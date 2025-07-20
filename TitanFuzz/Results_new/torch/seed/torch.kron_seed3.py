input = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
other = torch.tensor([[5, 6], [7, 8]], dtype=torch.float32)
output = torch.kron(input, other)