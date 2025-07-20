input_tensor = torch.randn(5, dtype=torch.float)
output_tensor = torch.Tensor.expm1_(input_tensor)