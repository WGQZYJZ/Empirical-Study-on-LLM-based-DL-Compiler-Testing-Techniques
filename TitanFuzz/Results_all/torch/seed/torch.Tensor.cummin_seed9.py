input_tensor = torch.randn(2, 3, 4, 5)
cummin_tensor = torch.Tensor.cummin(input_tensor, dim=2)