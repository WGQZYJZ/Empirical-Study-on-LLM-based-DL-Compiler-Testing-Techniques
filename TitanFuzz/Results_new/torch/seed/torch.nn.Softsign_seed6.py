input = Variable(torch.randn(1, 5))
output = torch.nn.Softsign()(input)