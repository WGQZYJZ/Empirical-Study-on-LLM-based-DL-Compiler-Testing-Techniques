A = torch.randn(2, 3, requires_grad=True)
B = torch.linalg.pinv(A)