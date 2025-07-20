input_tensor = torch.randn(4, 4)
cummax_tensor = torch.Tensor.cummax(input_tensor, dim=0)