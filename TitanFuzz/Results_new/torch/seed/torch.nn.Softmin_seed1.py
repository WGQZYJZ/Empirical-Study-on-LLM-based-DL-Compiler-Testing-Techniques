input = torch.randn(2, 3)
softmin = torch.nn.Softmin(dim=1)
output = softmin(input)