input = torch.tensor([1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1])
weights = torch.tensor([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
output = torch.bincount(input, weights=weights)