input_data = torch.randn(3, 3)
(eigen_values, eigen_vectors) = torch.eig(input_data, True)