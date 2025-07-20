dataset1 = torch.utils.data.TensorDataset(torch.rand(1000, 3), torch.rand(1000))
dataset2 = torch.utils.data.TensorDataset(torch.rand(1000, 3), torch.rand(1000))
dataset = torch.utils.data.ConcatDataset([dataset1, dataset2])
dataset = torch.utils.data.Subset(dataset, range(10))