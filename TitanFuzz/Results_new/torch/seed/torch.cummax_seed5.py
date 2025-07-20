input = torch.randn(3, 3)
output = torch.cummax(input, dim=0)
output = torch.cummax(input, dim=1)