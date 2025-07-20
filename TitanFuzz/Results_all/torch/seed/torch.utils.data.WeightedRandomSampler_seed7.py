input_data = np.arange(10)
weights = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
sampler = torch.utils.data.WeightedRandomSampler(weights, 3, replacement=False)
for idx in sampler:
    print(input_data[idx])