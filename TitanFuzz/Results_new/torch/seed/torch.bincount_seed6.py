input = torch.tensor([1, 1, 2, 3, 2, 3, 3, 4, 4, 5, 6, 7, 7, 8, 8, 8, 9, 10, 10])
torch.bincount(input)
weights = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
torch.bincount(input, weights=weights)