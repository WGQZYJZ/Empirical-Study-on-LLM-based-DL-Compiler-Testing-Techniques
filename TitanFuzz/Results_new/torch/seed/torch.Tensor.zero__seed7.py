x = torch.randn(2, 3)
y = torch.Tensor.zero_(x)
x = torch.randn(2, 3)
y = torch.Tensor.fill_(x, 2)
x = torch.randn(2, 3)
y = torch.Tensor.add_(x, 2)