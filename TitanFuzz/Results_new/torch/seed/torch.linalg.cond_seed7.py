A = torch.randn(4, 4)
A = torch.matmul(A.t(), A)
cond_A = torch.linalg.cond(A)
cond_A_p2 = torch.linalg.cond(A, p=2)
cond_A_pfro = torch.linalg.cond(A, p='fro')