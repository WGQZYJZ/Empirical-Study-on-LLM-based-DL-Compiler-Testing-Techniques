(N, K, M) = (10, 10, 10)
mat1 = torch.randn(N, K)
mat2 = torch.randn(K, M)
output = torch.sparse.mm(mat1, mat2)