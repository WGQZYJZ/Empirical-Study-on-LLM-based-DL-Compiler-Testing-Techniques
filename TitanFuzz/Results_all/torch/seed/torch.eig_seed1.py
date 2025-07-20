input_data = torch.randn(3, 3)
(eigenvalues, eigenvectors) = torch.eig(input_data, True)