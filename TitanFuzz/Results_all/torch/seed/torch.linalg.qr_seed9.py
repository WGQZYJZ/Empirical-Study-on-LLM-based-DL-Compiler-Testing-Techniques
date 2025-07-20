A = torch.rand(3, 4, dtype=torch.float, requires_grad=True)
(q, r) = torch.linalg.qr(A)