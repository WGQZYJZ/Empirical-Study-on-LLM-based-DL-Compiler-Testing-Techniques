A = torch.randn(3, 5)
(A_q, A_r) = torch.qr(A)
A = torch.randn(3, 3)
b = torch.randn(3, 2)
x = torch.triangular_solve(b, A)[0]