input_tensor = torch.arange(1, 11)
output_tensor = torch.Tensor.as_strided(input_tensor, (3, 3), (4, 1))