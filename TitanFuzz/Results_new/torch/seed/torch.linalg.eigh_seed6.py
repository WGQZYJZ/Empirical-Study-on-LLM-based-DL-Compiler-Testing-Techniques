A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
A = torch.from_numpy(A).float()
(eigen_values, eigen_vectors) = torch.linalg.eigh(A)