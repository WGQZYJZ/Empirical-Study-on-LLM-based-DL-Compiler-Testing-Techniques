input = torch.randn(3, 2)
output = torch.min(input, dim=1)
input = torch.randn(3, 2)
output = torch.min(input, dim=1, keepdim=True)