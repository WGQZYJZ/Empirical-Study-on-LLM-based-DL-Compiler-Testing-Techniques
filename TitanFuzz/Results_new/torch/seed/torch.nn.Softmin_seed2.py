input = torch.randn(2, 3)
output = torch.nn.Softmin(dim=1)(input)