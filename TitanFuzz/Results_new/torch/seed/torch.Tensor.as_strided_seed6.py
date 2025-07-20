input_tensor = torch.rand(5, 7)
output_tensor = torch.Tensor.as_strided(input_tensor, (3, 3), (4, 4))