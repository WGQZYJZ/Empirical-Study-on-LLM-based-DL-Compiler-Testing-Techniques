input = torch.randn(3, requires_grad=True)
other = torch.randn(3)
output = torch.ne(input, other)
x = torch.ones(2, 2, requires_grad=True)
y = (x + 2)
z = ((y * y) * 3)
out = z.mean()
a = torch.randn(2, 2)
a