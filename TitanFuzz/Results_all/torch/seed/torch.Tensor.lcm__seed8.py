input_tensor = torch.tensor([[2, 3, 4], [4, 5, 6]])
other = torch.tensor([[4, 6, 8], [8, 10, 12]])
torch.Tensor.lcm_(input_tensor, other)