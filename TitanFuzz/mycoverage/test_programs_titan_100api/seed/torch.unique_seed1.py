input_data = torch.tensor([1, 3, 2, 3])
(unique_data, inverse_data, counts_data) = torch.unique(input_data, sorted=True, return_inverse=True, return_counts=True)
input_data_2 = torch.tensor([[1, 3, 2, 3], [1, 3, 2, 3]])