input_data = torch.rand(5)
sampler = torch.utils.data.SequentialSampler(input_data)
for i in sampler:
    print(i)