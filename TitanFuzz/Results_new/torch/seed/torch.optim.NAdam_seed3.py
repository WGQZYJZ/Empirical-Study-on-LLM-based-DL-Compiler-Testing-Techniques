x = torch.randn(1, requires_grad=True)
y = torch.randn(1, requires_grad=True)
optimizer = torch.optim.NAdam([x, y], lr=0.002, betas=(0.9, 0.999), eps=1e-08, weight_decay=0, momentum_decay=0.004)