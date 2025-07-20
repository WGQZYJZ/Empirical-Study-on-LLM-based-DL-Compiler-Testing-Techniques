A = torch.randn(3, 3)
A = A.mm(A.t())
(e, v) = torch.symeig(A, True)