input_data = torch.rand(5)
sampler = torch.utils.data.RandomSampler(input_data)
for i in sampler:
    print(i)
input_data = torch.rand(5)
sampler = torch.utils.data.SequentialSampler(input_data)
for i in sampler:
    print(i)
input_data = torch.rand(5)
indices = [1, 3]
sampler = torch.utils.data.SubsetRandomSampler(indices)