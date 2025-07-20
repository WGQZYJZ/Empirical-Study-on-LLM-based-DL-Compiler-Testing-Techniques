input = torch.randn(3, 4)
output = torch.nn.Softmin(dim=1)(input)