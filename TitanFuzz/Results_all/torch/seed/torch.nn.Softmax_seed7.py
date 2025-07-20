input = Variable(torch.randn(1, 3))
softmax = torch.nn.Softmax(dim=1)
output = softmax(input)