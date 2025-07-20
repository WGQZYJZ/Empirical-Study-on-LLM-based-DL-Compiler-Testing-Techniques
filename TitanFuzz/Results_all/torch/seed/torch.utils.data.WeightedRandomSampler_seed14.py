weights = np.array([0.5, 0.5])
num_samples = 10
replacement = True
sampler = torch.utils.data.WeightedRandomSampler(weights, num_samples, replacement)
for (i, index) in enumerate(sampler):
    print('{}: {}'.format(i, index))