A = torch.randn(3, 3)
A
A_inv = torch.inverse(A)
A_inv
torch.mm(A, A_inv)
torch.mm(A_inv, A)