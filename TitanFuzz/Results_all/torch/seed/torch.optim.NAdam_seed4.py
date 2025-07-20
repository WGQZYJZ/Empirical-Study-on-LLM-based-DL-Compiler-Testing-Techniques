x = torch.tensor(1.0, requires_grad=True)
optimizer = torch.optim.NAdam([x], lr=0.002, betas=(0.9, 0.999), eps=1e-08, weight_decay=0, momentum_decay=0.004)
for i in range(1000):
    optimizer.zero_grad()
    y = (x ** 2)
    loss = y.sum()
    loss.backward()
    optimizer.step()
    print('step {}, x = {}, loss = {}'.format(i, x.item(), loss.item()))