input = torch.tensor([1, 3, 2, 3, 1, 2, 1, 3, 2, 1, 1, 1, 3, 2, 1])
(unique_output, inverse_output, count_output) = torch.unique(input, sorted=True, return_inverse=True, return_counts=True)