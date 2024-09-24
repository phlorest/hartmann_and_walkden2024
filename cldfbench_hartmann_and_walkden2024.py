import pathlib

import phlorest


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "hartmann_and_walkden2024"

    def cmd_makecldf(self, args):
        self.init(args)
        
        # Add summary tree (e.g. MCCT or Consensus)
        summary = self.raw_dir.read_tree('Tree_Full.con.tre', detranslate=True)
        args.writer.add_summary(summary, self.metadata, args.log)

        # Add posterior tree distribution
        # posterior = self.raw_dir.read_trees(
        #     'posterior.trees.gz',
        #     burnin=1001, sample=1000, detranslate=True)
        # args.writer.add_posterior(posterior, self.metadata, args.log)
        
        # Add nexus data
        data = self.raw_dir.read_nexus('full.nex')
        args.writer.add_data(data, self.characters, args.log)
