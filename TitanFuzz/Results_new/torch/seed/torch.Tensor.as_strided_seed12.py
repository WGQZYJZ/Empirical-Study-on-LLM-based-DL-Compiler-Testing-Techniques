input_tensor = torch.tensor([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])
size = (2, 3)
stride = (1, 3)
output_tensor = torch.Tensor.as_strided(input_tensor, size, stride)