weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sampler = torch.utils.data.WeightedRandomSampler(weights, 5)
for i in sampler:
    print(i)
sampler = torch.utils.data.WeightedRandomSampler(weights, 5, replacement=False)
for i in sampler:
    print(i)