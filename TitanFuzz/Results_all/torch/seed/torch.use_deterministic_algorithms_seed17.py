x = Variable(torch.randn(1, 1, 3, 3))
y = Variable(torch.randn(1, 1, 3, 3))
torch.use_deterministic_algorithms(mode=True)
torch.use_deterministic_algorithms(mode=False)