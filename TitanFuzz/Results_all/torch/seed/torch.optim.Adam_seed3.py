x = torch.randn(2, 2, requires_grad=True)
y = torch.randn(2, 2, requires_grad=True)
adam = torch.optim.Adam([x, y], lr=0.001, betas=(0.9, 0.999), eps=1e-08, weight_decay=0, amsgrad=False)
adam.step()