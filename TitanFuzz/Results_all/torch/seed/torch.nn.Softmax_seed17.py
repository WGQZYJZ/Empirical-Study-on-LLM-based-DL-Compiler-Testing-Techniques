x = Variable(torch.randn(2, 3))
softmax = torch.nn.Softmax(dim=1)
result = softmax(x)