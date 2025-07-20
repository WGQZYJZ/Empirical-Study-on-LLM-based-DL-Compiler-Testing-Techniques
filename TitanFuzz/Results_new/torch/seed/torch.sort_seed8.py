input = torch.randn(3, 5)
output = torch.sort(input)
output = torch.sort(input, dim=1)
output = torch.sort(input, dim=0, descending=True)