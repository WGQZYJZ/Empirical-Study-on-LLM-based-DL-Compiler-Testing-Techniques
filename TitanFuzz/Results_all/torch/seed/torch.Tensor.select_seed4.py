input_tensor = torch.randn(2, 3, 4)
output_tensor = torch.Tensor.select(input_tensor, dim=1, index=1)