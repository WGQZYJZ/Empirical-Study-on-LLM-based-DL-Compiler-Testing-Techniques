A = torch.randn(3, 3, requires_grad=True)
B = torch.linalg.pinv(A)
A.backward(torch.eye(3))