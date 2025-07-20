input_tensor = torch.randn(4, 4)
quantile_value = torch.Tensor.quantile(input_tensor, 0.5, dim=None, keepdim=False)