input_tensor = torch.randn(3, 4)
output_tensor = torch.Tensor.select(input_tensor, 0, 1)