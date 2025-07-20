x = torch.rand(4, 4)
y = torch.rand(4, 4)
z = torch.jit.annotate(torch.Tensor, None)
for i in range(10):
    z = (x + y)
    print(z)