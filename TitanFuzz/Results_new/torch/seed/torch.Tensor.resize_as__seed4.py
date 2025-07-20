input_tensor = torch.randn(3, 3)
output_tensor = torch.randn(5, 5)
torch.Tensor.resize_as_(input_tensor, output_tensor)