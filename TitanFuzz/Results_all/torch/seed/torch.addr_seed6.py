input = torch.randn(4, 4, dtype=torch.float)
vec1 = torch.randn(4, dtype=torch.float)
vec2 = torch.randn(4, dtype=torch.float)
output = torch.addr(input, vec1, vec2)