input_tensor = torch.randn(3, 3)
other = torch.randn(3, 3)
torch.Tensor.ge_(input_tensor, other)