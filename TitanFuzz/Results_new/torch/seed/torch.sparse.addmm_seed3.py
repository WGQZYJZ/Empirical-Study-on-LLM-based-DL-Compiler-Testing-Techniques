mat = torch.sparse.FloatTensor(3, 3).to_dense()
mat1 = torch.randn(3, 5)
mat2 = torch.randn(5, 3)
torch.sparse.addmm(mat, mat1, mat2, beta=1.0, alpha=1.0)