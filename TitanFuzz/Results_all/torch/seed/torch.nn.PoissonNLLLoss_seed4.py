x = torch.rand(10, 1)
y = torch.rand(10, 1)
loss = torch.nn.PoissonNLLLoss(reduction='none')(x, y)