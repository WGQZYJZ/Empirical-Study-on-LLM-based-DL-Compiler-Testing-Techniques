x = Variable(torch.ones(2, 2), requires_grad=True)
optimizer = torch.optim.Adadelta(params=[x], lr=0.001, rho=0.9, eps=1e-06, weight_decay=0)
optimizer.zero_grad()
optimizer.step()