data = list(range(10))
sampler = torch.utils.data.SequentialSampler(data)
for index in sampler:
    print(index)
data = list(range(10))
sampler = torch.utils.data.RandomSampler(data)
for index in sampler:
    print(index)