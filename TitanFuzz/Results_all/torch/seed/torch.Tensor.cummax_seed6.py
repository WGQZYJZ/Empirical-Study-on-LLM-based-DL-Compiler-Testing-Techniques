input_tensor = torch.randn(3, 3)
cummax_tensor = torch.Tensor.cummax(input_tensor, dim=0)