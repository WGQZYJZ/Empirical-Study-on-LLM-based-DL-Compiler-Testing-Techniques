input = torch.randn(10)
output = torch.special.i0(input)
output = torch.special.i0(input, out=input)