input = torch.tensor([1, 2, 3, 3, 4, 4, 4, 5, 6, 6, 6, 6, 7, 8, 8, 8, 8, 8, 8, 8])
(unique, indices) = torch.unique_consecutive(input, return_inverse=True)
(unique, indices, counts) = torch.unique_consecutive(input, return_inverse=True, return_counts=True)