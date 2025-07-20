input_tensor = torch.Tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
output_tensor = torch.Tensor.as_strided(input_tensor, (3, 2), (2, 1), 0)