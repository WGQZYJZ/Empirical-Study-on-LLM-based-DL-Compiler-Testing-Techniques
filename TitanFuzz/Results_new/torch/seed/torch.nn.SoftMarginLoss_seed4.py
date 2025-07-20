x = Variable(torch.randn(5, 10))
y = Variable(torch.randn(5, 10))
loss = torch.nn.SoftMarginLoss()