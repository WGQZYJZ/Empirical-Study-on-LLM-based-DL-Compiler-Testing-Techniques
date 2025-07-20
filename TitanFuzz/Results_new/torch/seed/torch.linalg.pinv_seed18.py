A = torch.randn(3, 3, dtype=torch.float32)
A_pinv = torch.linalg.pinv(A)