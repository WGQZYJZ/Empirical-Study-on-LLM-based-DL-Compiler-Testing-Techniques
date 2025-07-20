x = torch.randn(5, requires_grad=True)
y = torch.logit(x)
y.backward(torch.ones(5))