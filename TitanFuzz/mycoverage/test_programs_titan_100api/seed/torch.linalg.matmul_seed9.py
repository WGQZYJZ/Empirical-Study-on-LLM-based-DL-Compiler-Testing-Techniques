a = torch.randn(2, 3, requires_grad=True)
b = torch.randn(3, 4, requires_grad=True)
c = torch.linalg.matmul(a, b)