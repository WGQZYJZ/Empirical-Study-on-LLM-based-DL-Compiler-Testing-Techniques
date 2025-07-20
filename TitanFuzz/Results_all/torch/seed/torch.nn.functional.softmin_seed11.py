input = Variable(torch.randn(2, 3))
output = torch.nn.functional.softmin(input, dim=1)