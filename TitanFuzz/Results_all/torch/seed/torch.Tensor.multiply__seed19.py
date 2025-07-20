input_tensor = torch.randn(4, 4)
torch.Tensor.multiply_(input_tensor, 2)
input_tensor = torch.randn(4, 4)
torch.Tensor.mul_(input_tensor, input_tensor)