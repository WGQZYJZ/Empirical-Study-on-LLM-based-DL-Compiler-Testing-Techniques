mat1 = torch.sparse.FloatTensor(3, 3).to_dense()
mat2 = torch.sparse.FloatTensor(3, 3).to_dense()
torch.sparse.mm(mat1, mat2)