input_tensor = torch.tensor([[3, 3, 3], [3, 3, 3]], dtype=torch.int32)
other_tensor = torch.tensor([[2, 2, 2], [2, 2, 2]], dtype=torch.int32)
torch.Tensor.gcd_(input_tensor, other_tensor)