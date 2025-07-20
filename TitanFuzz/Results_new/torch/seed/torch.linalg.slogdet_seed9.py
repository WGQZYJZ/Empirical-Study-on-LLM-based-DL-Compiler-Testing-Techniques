A = torch.randn(3, 3)
(sign, logdet) = torch.linalg.slogdet(A)
A = torch.randn(4, 4)
(sign, logdet) = torch.linalg.slogdet(A)