input = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
other = torch.tensor([[1, 1, 1], [1, 1, 1]], dtype=torch.float32)
result = torch.sub(input, other)