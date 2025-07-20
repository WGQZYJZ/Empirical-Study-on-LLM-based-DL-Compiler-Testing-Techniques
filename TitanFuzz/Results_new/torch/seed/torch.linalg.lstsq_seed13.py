A = torch.randn(3, 3)
B = torch.randn(3, 1)
X = torch.linalg.lstsq(A, B)