input_tensor = torch.randn(3, 3)
cummin_tensor = torch.Tensor.cummin(input_tensor, dim=1)