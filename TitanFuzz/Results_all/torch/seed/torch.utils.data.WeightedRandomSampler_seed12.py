weights = [1, 2, 3, 4, 5]
sampler = torch.utils.data.WeightedRandomSampler(weights, 5, replacement=True)
for i in range(5):
    print(next(iter(sampler)))