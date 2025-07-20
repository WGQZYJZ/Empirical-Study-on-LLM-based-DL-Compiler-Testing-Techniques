input = Variable(torch.randn(4, 4))
relu6 = torch.nn.ReLU6()
output = relu6(input)