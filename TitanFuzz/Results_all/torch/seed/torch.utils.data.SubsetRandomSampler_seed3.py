input_data = torch.randn(100, 2)
label = torch.randint(0, 2, (100,))
sampler = torch.utils.data.SubsetRandomSampler(range(0, 50))
loader = torch.utils.data.DataLoader(dataset=torch.utils.data.TensorDataset(input_data, label), batch_size=10, sampler=sampler)
for (batch_idx, (data, target)) in enumerate(loader):
    print('Batch:', batch_idx, 'data:', data, 'target:', target)