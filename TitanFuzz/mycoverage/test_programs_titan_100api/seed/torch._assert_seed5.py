a = torch.randn(1, requires_grad=True)
b = torch.randn(1, requires_grad=True)
c = torch.randn(1)
torch._assert((a.shape == b.shape), 'a and b must have the same shape')
torch._assert((a.shape == c.shape), 'a and c must have the same shape')