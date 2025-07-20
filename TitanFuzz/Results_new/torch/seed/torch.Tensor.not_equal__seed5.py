input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float)
other = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float)
torch.Tensor.not_equal_(input_tensor, other)