input_data = torch.rand(100, 1)
batch_sampler = torch.utils.data.BatchSampler(sampler=torch.utils.data.RandomSampler(input_data), batch_size=5, drop_last=False)
for batch_indices in batch_sampler:
    print(batch_indices)