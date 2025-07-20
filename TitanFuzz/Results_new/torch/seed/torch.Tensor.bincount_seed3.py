input_tensor = torch.Tensor([1, 2, 3, 4, 5, 6, 6, 6])
output_tensor = torch.Tensor.bincount(input_tensor)
output_tensor = torch.Tensor.bincount(input_tensor, weights=input_tensor)