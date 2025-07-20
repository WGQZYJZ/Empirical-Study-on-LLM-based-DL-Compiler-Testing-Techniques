input_data = np.arange(20).reshape(10, 2)
batch_sampler = torch.utils.data.BatchSampler(sampler=torch.utils.data.SequentialSampler(input_data), batch_size=3, drop_last=False)
for batch in batch_sampler:
    print(batch)