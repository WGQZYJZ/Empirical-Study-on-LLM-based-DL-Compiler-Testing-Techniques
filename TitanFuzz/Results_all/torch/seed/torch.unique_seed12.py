input_data = torch.tensor([[1, 3, 3], [2, 2, 1], [3, 1, 1]])
(unique_data, inverse_data, counts_data) = torch.unique(input_data, sorted=True, return_inverse=True, return_counts=True, dim=0)