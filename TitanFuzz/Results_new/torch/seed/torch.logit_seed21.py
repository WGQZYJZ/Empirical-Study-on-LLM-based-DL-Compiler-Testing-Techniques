x = torch.randn(5, 3)
torch.logit(x)
torch.logit(x, eps=1e-06)
y = torch.randn(5, 3)
torch.logit(x, out=y)
y
torch.logit(x, eps=1e-06, out=y)
y
torch.logit(x, out=y, eps=1e-06)
y