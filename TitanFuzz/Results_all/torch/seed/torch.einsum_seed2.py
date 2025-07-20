A = torch.tensor([[1, 2, 3], [4, 5, 6]])
B = torch.tensor([[7, 8, 9], [10, 11, 12]])
C = torch.einsum('ik,jk->ijk', A, B)