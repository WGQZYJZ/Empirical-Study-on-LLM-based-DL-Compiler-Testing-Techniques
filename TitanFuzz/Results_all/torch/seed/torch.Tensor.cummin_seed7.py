input_tensor = torch.randn(3, 4)
cummin_tensor = torch.Tensor.cummin(input_tensor, dim=1)