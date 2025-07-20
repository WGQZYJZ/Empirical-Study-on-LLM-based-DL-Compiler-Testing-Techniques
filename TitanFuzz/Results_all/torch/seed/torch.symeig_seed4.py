A = torch.Tensor([[1, 2, 3], [2, 4, 5], [3, 5, 6]])
(eigen_values, eigen_vectors) = torch.symeig(A, eigenvectors=True)