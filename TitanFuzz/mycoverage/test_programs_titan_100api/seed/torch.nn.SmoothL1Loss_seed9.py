x = torch.tensor([(- 1.0), 1.0, 2.0, 3.0, 4.0, 5.0])
y = torch.tensor([(- 1.0), 1.0, 2.0, 3.0, 4.0, 5.0])
smoothL1Loss = torch.nn.SmoothL1Loss()
loss = smoothL1Loss(x, y)