x = Variable(torch.randn(2, 3))
y = torch.nn.functional.selu(x)