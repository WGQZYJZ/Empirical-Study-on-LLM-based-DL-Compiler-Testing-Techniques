x = Variable(torch.ones(2, 2), requires_grad=True)
optimizer = torch.optim.NAdam([x], lr=0.002, betas=(0.9, 0.999), eps=1e-08, weight_decay=0, momentum_decay=0.004)
optimizer.zero_grad()
y = x.sum()
y.backward()
optimizer.step()