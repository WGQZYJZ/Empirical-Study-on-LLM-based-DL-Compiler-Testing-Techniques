input = torch.tensor([1, 3, 2, 3, 4, 4, 5, 1, 2, 6, 5, 7, 7, 7, 8, 9, 9, 9, 10])
(unique, inverse, counts) = torch.unique(input, sorted=True, return_inverse=True, return_counts=True, dim=None)