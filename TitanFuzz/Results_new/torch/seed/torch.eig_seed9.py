input = torch.randn(3, 3)
(eigen_values, eigen_vectors) = torch.eig(input, eigenvectors=True)
eigen_values = torch.eig(input, eigenvectors=False)