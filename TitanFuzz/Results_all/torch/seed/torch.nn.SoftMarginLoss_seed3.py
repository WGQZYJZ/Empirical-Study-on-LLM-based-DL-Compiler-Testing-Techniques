input = Variable(torch.randn(3, 5), requires_grad=True)
target = Variable(torch.randn(3, 5))
loss = torch.nn.SoftMarginLoss()
output = loss(input, target)