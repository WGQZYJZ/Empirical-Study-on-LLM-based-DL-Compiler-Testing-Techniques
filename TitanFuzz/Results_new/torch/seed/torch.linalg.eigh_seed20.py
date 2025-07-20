A = torch.randn(8, 8)
A = A.mm(A.t())
(e, v) = torch.linalg.eigh(A)