A = torch.arange(6).view(2, 3)
B = torch.arange(6).view(3, 2)
torch.einsum('ij,jk->ik', (A, B))