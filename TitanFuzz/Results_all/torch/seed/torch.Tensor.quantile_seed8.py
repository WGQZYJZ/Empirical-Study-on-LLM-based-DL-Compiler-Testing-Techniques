input_tensor = torch.randn(3, 3)
quantile_value = torch.Tensor.quantile(input_tensor, 0.5)