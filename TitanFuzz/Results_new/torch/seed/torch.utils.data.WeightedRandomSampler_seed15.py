weights = [0.2, 0.3, 0.5]
num_samples = 10
replacement = True
sampler = torch.utils.data.WeightedRandomSampler(weights, num_samples, replacement)
for i in range(10):
    print(next(iter(sampler)))