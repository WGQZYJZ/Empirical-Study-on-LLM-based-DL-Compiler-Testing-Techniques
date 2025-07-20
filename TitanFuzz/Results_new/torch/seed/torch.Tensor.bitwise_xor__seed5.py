input_tensor = torch.tensor([[1, 0, 1], [0, 1, 0]])
other = torch.tensor([[1, 0, 0], [0, 0, 1]])
torch.Tensor.bitwise_xor_(input_tensor, other)