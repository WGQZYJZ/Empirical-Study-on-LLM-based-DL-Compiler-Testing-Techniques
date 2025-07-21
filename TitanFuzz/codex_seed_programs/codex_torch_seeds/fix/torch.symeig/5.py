'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.symeig\ntorch.symeig(input, eigenvectors=False, upper=True, *, out=None)\n'
import torch
input_data = torch.randn(3, 3)
print('Input data: ', input_data)
(eigen_values, eigen_vectors) = torch.symeig(input_data, eigenvectors=True)
print('Eigen values: ', eigen_values)
print('Eigen vectors: ', eigen_vectors)