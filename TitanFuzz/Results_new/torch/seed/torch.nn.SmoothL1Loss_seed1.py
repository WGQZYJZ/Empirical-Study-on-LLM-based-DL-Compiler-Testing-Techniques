x = torch.randn((3, 2))
y = torch.randn((3, 2))
loss_fn = torch.nn.SmoothL1Loss()
loss = loss_fn(x, y)