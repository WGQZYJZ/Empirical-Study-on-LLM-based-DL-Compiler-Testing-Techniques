_input_tensor = torch.tensor([[0, 1, 0], [0, 0, 1]])
other = torch.tensor([[0, 0, 1], [0, 1, 0]])
torch.Tensor.logical_or_(_input_tensor, other)