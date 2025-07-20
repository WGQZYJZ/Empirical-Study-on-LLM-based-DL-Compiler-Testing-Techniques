input_tensor = torch.tensor([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
weights = torch.tensor([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
output_tensor = torch.Tensor.bincount(input_tensor, weights=weights, minlength=10)