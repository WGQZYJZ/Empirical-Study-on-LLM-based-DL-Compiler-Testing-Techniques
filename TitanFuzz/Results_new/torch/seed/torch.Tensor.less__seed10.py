input_tensor = torch.randn(3, 3)
other_tensor = torch.randn(3, 3)
less_tensor = torch.Tensor.less_(input_tensor, other_tensor)