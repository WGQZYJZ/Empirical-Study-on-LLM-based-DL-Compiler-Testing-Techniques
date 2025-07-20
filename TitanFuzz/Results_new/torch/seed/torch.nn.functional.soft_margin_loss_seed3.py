x = torch.randn(10, 10)
y = torch.randn(10, 10)
loss = torch.nn.functional.soft_margin_loss(x, y)