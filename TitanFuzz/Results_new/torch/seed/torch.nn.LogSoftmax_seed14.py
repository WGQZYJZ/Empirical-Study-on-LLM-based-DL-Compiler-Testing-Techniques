input = Variable(torch.randn(5), requires_grad=True)
output = torch.nn.LogSoftmax(input)