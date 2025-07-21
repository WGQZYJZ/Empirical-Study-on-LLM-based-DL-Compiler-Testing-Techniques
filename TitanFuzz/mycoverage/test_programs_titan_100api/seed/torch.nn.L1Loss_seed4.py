x = torch.tensor([[1, 2, 3], [2, 3, 4]], dtype=torch.float32)
y = torch.tensor([[1, 2, 3], [2, 3, 4]], dtype=torch.float32)
loss_fn = torch.nn.L1Loss(reduction='mean')
loss = loss_fn(x, y)