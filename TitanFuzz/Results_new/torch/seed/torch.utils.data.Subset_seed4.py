input_data = torch.arange(0, 10)
sampler = torch.utils.data.Subset(input_data, [1, 3, 5, 7])
for i in sampler:
    print(i)