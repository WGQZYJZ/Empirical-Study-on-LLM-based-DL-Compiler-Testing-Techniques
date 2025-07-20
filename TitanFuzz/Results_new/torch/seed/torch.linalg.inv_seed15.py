A = torch.randn(2, 2)
A_inv = torch.linalg.inv(A)
I = torch.mm(A, A_inv)