input_tensor = torch.tensor([[1, 0, 1], [0, 0, 1]])
other = torch.tensor([[1, 1, 0], [1, 0, 0]])
torch.Tensor.bitwise_xor_(input_tensor, other)