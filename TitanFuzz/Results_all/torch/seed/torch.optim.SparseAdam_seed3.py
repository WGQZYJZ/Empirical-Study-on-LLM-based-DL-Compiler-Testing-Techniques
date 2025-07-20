(n, m) = (10, 20)
x = torch.randn(n, m)
y = torch.randn(n, m)
torch.optim.SparseAdam(x, lr=0.001, betas=(0.9, 0.999), eps=1e-08)