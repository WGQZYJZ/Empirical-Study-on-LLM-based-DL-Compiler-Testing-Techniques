input = torch.randn(2, 3)
vec = torch.randn(3)
output = torch.mv(input, vec)
output = torch.mv(input, vec, out=torch.zeros(2))