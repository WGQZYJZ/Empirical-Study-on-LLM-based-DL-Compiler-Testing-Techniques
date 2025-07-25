np.random.seed(0)
x = np.random.rand(100)
y = np.random.rand(100)
loss = torch.nn.HuberLoss(reduction='mean', delta=1.0)
loss(torch.tensor(x), torch.tensor(y))
loss = torch.nn.HuberLoss(reduction='mean', delta=0.01)
loss(torch.tensor(x), torch.tensor(y))