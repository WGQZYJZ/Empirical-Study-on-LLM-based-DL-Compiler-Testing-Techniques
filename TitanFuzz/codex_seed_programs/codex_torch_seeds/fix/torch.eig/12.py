'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.eig\ntorch.eig(input, eigenvectors=False, *, out=None)\n'
import torch
input_data = torch.randn(3, 3)
print('Input data:\n', input_data)
(eigen_values, eigen_vectors) = torch.eig(input_data, True)
print('Eigen values: ', eigen_values)
print('Eigen vectors: ', eigen_vectors)