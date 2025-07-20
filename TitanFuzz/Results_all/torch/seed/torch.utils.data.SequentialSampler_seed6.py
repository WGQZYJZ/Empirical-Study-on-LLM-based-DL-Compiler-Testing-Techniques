dataset = torch.utils.data.TensorDataset(torch.randn(100, 3), torch.randn(100))
sampler = torch.utils.data.SequentialSampler(dataset)
dataloader = torch.utils.data.DataLoader(dataset, batch_size=4, sampler=sampler)
for (i, (inputs, labels)) in enumerate(dataloader):
    print(inputs, labels)