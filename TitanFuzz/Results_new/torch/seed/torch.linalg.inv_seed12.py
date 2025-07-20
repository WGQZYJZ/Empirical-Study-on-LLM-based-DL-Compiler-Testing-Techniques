A = torch.rand(2, 2)
B = torch.linalg.inv(A)
C = torch.matmul(A, B)