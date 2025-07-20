input_tensor = torch.Tensor([[0, 0, 1, 1], [1, 0, 1, 0], [0, 1, 1, 0], [1, 0, 1, 1]])
other = torch.Tensor([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [1, 0, 1, 1]])
torch.Tensor.bitwise_or(input_tensor, other)