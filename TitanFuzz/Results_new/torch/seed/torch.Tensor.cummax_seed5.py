input_tensor = torch.randn(3, 4)
cummax_tensor = torch.Tensor.cummax(input_tensor, dim=1)