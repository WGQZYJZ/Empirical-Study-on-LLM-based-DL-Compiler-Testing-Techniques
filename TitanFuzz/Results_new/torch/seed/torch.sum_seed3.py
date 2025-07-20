input = torch.randn(10, 10)
output = torch.sum(input, dim=0)
output = torch.sum(input, dim=1)
output = torch.sum(input, dim=1, keepdim=True)