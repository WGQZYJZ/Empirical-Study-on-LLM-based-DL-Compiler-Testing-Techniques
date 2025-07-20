input = Variable(torch.randn(20, 20).double(), requires_grad=False)
target = Variable(torch.randn(10, 20).double(), requires_grad=False)
params = [input, target]
learning_rate = 0.01
lambd = 0.0001
alpha = 0.75
t0 = 1000000.0
weight_decay = 0
optimizer = torch.optim.ASGD(params, lr=learning_rate, lambd=lambd, alpha=alpha, t0=t0, weight_decay=weight_decay)