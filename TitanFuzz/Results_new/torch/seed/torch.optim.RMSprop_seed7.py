x = torch.randn(1, requires_grad=True)
y = (x ** 2)
opt = torch.optim.RMSprop([x], lr=0.01, alpha=0.99, eps=1e-08, weight_decay=0, momentum=0, centered=False)
for i in range(100):
    y = (x ** 2)
    y.backward()
    opt.step()
    opt.zero_grad()