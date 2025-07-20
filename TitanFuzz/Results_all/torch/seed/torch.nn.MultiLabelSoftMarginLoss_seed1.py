input = torch.randn(3, requires_grad=True)
target = torch.empty(3).random_(2)
loss = torch.nn.MultiLabelSoftMarginLoss()
output = loss(input, target)
input = torch.randn(3, requires_grad=True)
target = torch.empty(3).random_(2)
loss = torch.nn