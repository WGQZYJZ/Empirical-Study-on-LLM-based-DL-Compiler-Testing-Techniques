params = [torch.tensor([1.0, 2.0], requires_grad=True)]
optimizer = torch.optim.ASGD(params, lr=0.01, lambd=0.0001, alpha=0.75, t0=1000000.0, weight_decay=0)