A = torch.randn(3, 3)
B = torch.randn(3, 2)
output = torch.linalg.lstsq(A, B)