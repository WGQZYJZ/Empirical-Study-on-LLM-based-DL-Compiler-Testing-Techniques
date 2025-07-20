A = torch.rand(2, 2)
B = torch.linalg.inv_ex(A)
C = torch.linalg.inv(A)
D = torch.linalg.pinv(A)