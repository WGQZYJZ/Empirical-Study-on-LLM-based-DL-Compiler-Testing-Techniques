input_tensor = torch.randn(3, 3)
other = torch.tensor([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]])
torch.Tensor.ge_(input_tensor, other)