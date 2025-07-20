A = torch.sparse.FloatTensor(3, 3).to_dense()
B = torch.sparse.FloatTensor(3, 3).to_dense()
C = torch.sparse.FloatTensor(3, 3).to_dense()
torch.sparse.addmm(A, B, C)