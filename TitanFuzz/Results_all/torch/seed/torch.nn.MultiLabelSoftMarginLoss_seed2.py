N = 2
input = Variable(torch.randn(N, 10))
target = Variable(torch.FloatTensor(N, 10).random_(2))
loss = torch.nn.MultiLabelSoftMarginLoss()
output = loss(input, target)