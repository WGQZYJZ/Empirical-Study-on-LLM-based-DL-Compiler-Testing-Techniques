input_data = torch.randn(10, 3, 32, 32)
batch_sampler = torch.utils.data.BatchSampler(sampler=torch.utils.data.SequentialSampler(range(10)), batch_size=3, drop_last=True)
for indices in batch_sampler:
    print(indices)
    print(input_data[indices])