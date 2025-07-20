x = torch.tensor([1.0], requires_grad=True)
y = torch.tensor([2.0], requires_grad=True)
optimizer = torch.optim.Adadelta([x, y], lr=1.0, rho=0.9, eps=1e-06, weight_decay=0)
optimizer.step()