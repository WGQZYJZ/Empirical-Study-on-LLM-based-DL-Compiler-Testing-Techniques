input = torch.randn(10, 3)
target = torch.randn(10, 3)
loss = torch.nn.functional.huber_loss(input, target, reduction='mean', delta=1.0)