input_tensor = torch.randn(3, 3)
output_tensor = torch.Tensor.rot90(input_tensor, 1, (0, 1))