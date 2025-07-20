x = torch.randn(3, requires_grad=True)
y = (x * 2)
while (y.data.norm() < 1000):
    y = (y * 2)
torch.set_printoptions(precision=10)