input = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
weights = torch.tensor([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
minlength = 0
result = torch.bincount(input, weights, minlength)