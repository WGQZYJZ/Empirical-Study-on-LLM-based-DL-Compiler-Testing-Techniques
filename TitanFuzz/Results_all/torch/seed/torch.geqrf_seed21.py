input = torch.randn(3, 3)
output = torch.geqrf(input)
vec1 = torch.randn(3)
vec2 = torch.randn(3)
output = torch.ger(vec1, vec2)
A = torch