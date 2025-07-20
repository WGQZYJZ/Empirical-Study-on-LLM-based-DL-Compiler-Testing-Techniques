x = torch.randn(1, 1)
y = torch.randn(1, 1)
loss = torch.nn.functional.huber_loss(x, y)