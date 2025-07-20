x = torch.randn(1, 1, 10, 10)
y = torch.randn(1, 1, 10, 10)
torch.nn.functional.l1_loss(x, y)