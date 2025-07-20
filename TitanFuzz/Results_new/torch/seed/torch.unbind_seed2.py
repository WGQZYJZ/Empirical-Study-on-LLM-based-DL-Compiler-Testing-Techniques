input = torch.randn(2, 3)
output = torch.unbind(input, dim=0)
output = torch.unbind(input, dim=1)