x = torch.randn(1, requires_grad=True)
w = torch.randn(1, requires_grad=True)
b = torch.randn(1, requires_grad=True)
with torch.no_grad():
    y = ((w * x) + b)