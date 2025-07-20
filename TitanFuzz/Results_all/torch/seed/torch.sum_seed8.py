input = torch.randn(2, 3)
output = torch.sum(input, dim=0)
output = torch.sum(input, dim=1)