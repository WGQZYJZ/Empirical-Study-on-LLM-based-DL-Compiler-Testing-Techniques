input = torch.tensor([[1, 3, 3, 2, 1], [1, 3, 2, 1, 3]])
(unique_output, inverse_output, count_output) = torch.unique(input, sorted=True, return_inverse=True, return_counts=True, dim=0)