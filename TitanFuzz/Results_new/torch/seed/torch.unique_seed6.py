input = torch.tensor([1, 3, 2, 3, 1])
output = torch.unique(input)
(output, inverse_indices) = torch.unique(input, return_inverse=True)
(output, inverse_indices, counts) = torch.unique(input, return_inverse=True, return_counts=True)