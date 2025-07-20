input = torch.tensor([1, 1, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5])
(unique_input, inverse_input, counts_input) = torch.unique_consecutive(input, return_inverse=True, return_counts=True)