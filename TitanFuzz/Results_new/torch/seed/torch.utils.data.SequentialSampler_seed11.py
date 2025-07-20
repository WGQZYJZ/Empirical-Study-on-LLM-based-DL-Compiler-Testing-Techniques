data_source = torch.randn(10)
sampler = torch.utils.data.SequentialSampler(data_source)
for i in sampler:
    print(i)