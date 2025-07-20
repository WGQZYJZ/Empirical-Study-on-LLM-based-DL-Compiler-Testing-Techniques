A = torch.randn(3, 2)
(U, S, V) = torch.linalg.svd(A)
A = torch.randn(3, 3)
(U, S, V) = torch.linalg.svd(A)