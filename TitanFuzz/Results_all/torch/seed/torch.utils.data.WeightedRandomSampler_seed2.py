input_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
sampler = torch.utils.data.WeightedRandomSampler(weights, 1)
for i in range(10):
    print(sampler.__iter__().__next__())