x = torch.randn(1, 2, 3)
y = torch.randn(1, 2, 3)
loss = torch.nn.functional.l1_loss(x, y)