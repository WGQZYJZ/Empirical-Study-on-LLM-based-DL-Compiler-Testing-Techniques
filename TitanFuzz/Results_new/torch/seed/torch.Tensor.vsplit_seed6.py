input_tensor = torch.randn(2, 6)
split_tensor = torch.Tensor.vsplit(input_tensor, 3)