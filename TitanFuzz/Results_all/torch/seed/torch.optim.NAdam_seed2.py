x = torch.randn(10, 5)
y = torch.randn(10, 5)
optimizer = torch.optim.NAdam(params=[x, y], lr=0.002, betas=(0.9, 0.999), eps=1e-08, weight_decay=0, momentum_decay=0.004)