input = torch.randn(3, 5, requires_grad=True)
other = torch.randn(5, 6, requires_grad=True)
output = torch.matmul(input, other)