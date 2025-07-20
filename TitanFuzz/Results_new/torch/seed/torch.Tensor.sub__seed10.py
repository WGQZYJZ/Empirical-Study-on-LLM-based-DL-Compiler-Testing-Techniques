input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
other = torch.tensor([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
torch.Tensor.sub_(input_tensor, other)