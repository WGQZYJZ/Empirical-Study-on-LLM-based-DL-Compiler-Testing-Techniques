input_tensor = torch.rand(3, 5)
quantile_value = torch.Tensor.quantile(input_tensor, 0.5, dim=1, keepdim=True)