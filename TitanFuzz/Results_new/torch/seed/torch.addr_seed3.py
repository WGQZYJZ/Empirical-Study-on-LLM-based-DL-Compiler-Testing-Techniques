input = torch.randn(3, 3, requires_grad=True)
vec1 = torch.randn(3, requires_grad=True)
vec2 = torch.randn(3, requires_grad=True)
output = torch.addr(input, vec1, vec2)
input = torch.randn(3, 3, requires_grad=True)
vec1 = torch.randn(3, requires_grad=True)
vec2 = torch.randn(3, requires_grad=True)
output = torch.addcdiv(input, 1, vec1, vec2)