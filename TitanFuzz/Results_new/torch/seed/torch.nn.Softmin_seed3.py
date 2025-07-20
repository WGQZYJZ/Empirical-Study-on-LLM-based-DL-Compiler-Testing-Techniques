input = Variable(torch.randn(3, 5), requires_grad=True)
output = torch.nn.Softmin(dim=1)(input)