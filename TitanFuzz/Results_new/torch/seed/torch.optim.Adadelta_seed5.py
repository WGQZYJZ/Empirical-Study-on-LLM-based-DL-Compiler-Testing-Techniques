x = torch.tensor(data=[2.0, 3.0], requires_grad=True)
y = torch.tensor(data=[4.0, 6.0], requires_grad=True)
optimizer = torch.optim.Adadelta(params=[x, y], lr=1.0, rho=0.9, eps=1e-06, weight_decay=0)