input_data = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
unique_data = torch.unique_consecutive(input_data, return_inverse=False, return_counts=False, dim=None)