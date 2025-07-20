input_tensor = torch.randn(4, 3)
output_tensor = torch.Tensor.select(input_tensor, 1, 0)