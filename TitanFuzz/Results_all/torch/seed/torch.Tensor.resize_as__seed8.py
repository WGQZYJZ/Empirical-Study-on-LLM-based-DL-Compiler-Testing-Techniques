input_tensor = torch.randn(2, 3, 4, 5)
other_tensor = torch.randn(2, 3, 4, 5)
torch.Tensor.resize_as_(input_tensor, other_tensor)