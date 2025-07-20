input_tensor = torch.randn(2, 3)
tensor = torch.randn(3, 2)
torch.Tensor.resize_as_(input_tensor, tensor)