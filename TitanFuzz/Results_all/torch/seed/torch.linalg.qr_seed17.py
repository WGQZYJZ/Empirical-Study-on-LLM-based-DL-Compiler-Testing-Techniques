A = torch.randn(2, 3)
(q, r) = torch.linalg.qr(A)
(q, r) = torch.linalg.qr(A, out=(torch.empty(2, 3), torch.empty(2, 3)))