input = torch.rand(2, 3)
binary_data = torch.bernoulli(input)
probability = torch.tensor([0.2, 0.5, 0.7])
binary_data = torch.bernoulli(probability)