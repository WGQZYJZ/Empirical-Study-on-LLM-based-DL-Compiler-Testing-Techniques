input_data = torch.randn(2, 2)
(eigen_values, eigen_vectors) = torch.eig(input_data, eigenvectors=True)
eigen_values = torch.eig(input_data, eigenvectors=False)
input_data = torch.randn(2, 3, 4)