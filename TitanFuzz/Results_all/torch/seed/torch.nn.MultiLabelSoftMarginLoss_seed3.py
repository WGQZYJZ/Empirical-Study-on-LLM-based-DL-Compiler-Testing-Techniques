input = torch.randn(3, 5, requires_grad=True)
target = torch.empty(3, 5).random_(2)
loss = torch.nn.MultiLabelSoftMarginLoss()
output = loss(input, target)