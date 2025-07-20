A = torch.randn(3, 3)
A = torch.matmul(A, A.t())
(eigen_values, eigen_vectors) = torch.linalg.eigh(A)