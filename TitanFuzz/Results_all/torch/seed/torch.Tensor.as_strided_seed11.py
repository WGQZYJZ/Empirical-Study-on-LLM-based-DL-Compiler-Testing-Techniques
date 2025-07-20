input_tensor = torch.arange(1, 17).view(4, 4)
output_tensor = torch.Tensor.as_strided(input_tensor, (8, 2), (8, 4))