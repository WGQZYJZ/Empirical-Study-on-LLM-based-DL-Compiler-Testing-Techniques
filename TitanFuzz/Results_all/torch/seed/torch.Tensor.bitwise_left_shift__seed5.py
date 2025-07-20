input_tensor = torch.tensor([[1, 0, 1, 1], [0, 0, 1, 1]])
other = torch.tensor([[1, 0, 1, 1], [0, 0, 1, 1]])
torch.Tensor.bitwise_left_shift_(input_tensor, other)