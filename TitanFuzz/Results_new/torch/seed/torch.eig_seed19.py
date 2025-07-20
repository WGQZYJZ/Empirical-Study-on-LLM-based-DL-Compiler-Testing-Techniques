input = torch.randn(2, 2)
output = torch.eig(input)
output = torch.eig(input, True)