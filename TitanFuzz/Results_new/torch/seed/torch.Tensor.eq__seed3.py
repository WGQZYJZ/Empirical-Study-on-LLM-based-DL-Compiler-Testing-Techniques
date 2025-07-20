input_tensor = torch.tensor([[0, 1, 1], [1, 1, 0]])
other = torch.tensor([[1, 1, 0], [1, 0, 1]])
torch.Tensor.eq_(input_tensor, other)
input_tensor = torch.tensor([[0, 1, 1], [1, 1, 0]])