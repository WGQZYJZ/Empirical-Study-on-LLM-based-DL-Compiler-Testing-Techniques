input_tensor = torch.randn(2, 3, 4, 5)
target_tensor = torch.randn(2, 2, 3, 4, 5)
torch.Tensor.resize_as_(input_tensor, target_tensor)