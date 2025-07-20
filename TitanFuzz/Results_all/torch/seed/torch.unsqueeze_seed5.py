input = torch.randn(1, 1, 3)
output = torch.unsqueeze(input, dim=0)
output = torch.unsqueeze(input, dim=1)
output = torch.unsqueeze(input, dim=2)