x = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])
y = torch.tensor([2.0, 4.0, 6.0, 8.0, 10.0])
loss = torch.nn.HuberLoss(reduction='mean', delta=1.0)
output = loss(x, y)