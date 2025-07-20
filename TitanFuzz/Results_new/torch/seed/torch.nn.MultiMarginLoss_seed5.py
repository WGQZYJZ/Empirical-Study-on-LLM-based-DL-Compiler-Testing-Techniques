x = Variable(torch.randn(5, 3))
y = Variable(torch.LongTensor(5).random_(3))
loss = torch.nn.MultiMarginLoss()
output = loss(x, y)