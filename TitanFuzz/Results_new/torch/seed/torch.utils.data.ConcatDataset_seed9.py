dataset1 = torch.randn(100, 2)
dataset2 = torch.randn(100, 2)
dataset = torch.utils.data.ConcatDataset([dataset1, dataset2])