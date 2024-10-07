import pathlib

import phlorest


REPLACEMENTS = {
    'Basaá': 'Basaa',
    'DidaLakotadiéko': 'DidaLakotadieko',
    'Guébie': 'Guebie',
    'Mundurukú': 'Munduruku',
    'TupíTupinambá': 'TupiTupinamba',
    'Yémba': 'Yemba',
    'mɔ́dӡúkrù': 'Moduokru'
}

def fix(text):
    for old, new in REPLACEMENTS.items():
        text = text.replace(old, new)
    return text


def to_nexus(text):
    trees = ['tree %d = [&R] %s' % (i, fix(t)) for (i, t) in enumerate(text.split("\n"), 1) if len(t)]
    return "#NEXUS\nbegin trees;\n%s\nend;\n" % "\n".join(trees)


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "hartmann_and_walkden2024"

    def cmd_makecldf(self, args):
        self.init(args)
        
        # Add summary tree (e.g. MCCT or Consensus)
        summary = self.raw_dir.read_tree('Tree_Full.con.tre', preprocessor=fix, detranslate=False)
        args.writer.add_summary(summary, self.metadata, args.log)

        # Add posterior tree distribution (n=10002)
        posterior = self.raw_dir.read_trees(
            'PosteriorTrees_Full.posterior.tree.gz',
            burnin=1001, sample=1000, detranslate=False, preprocessor=to_nexus)
        args.writer.add_posterior(posterior, self.metadata, args.log)
        
        # Add nexus data
        data = self.raw_dir.read_nexus('full.nex', preprocessor=fix)
        args.writer.add_data(data, self.characters, args.log)
