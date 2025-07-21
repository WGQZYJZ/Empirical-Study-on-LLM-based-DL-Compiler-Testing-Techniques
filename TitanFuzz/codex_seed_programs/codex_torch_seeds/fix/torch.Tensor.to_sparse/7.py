'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.to_sparse\ntorch.Tensor.to_sparse(_input_tensor, sparseDims)\n'
import torch
import torch
input_tensor = torch.tensor([[1, 0, 0], [0, 2, 0], [3, 0, 0], [0, 0, 0], [0, 0, 4]])
output_tensor = input_tensor.to_sparse()
print('input_tensor is: \n', input_tensor)
print('output_tensor is: \n', output_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.to_sparse\ntorch.Tensor.to_sparse(_input_tensor, sparseDims)\n'
import torch
import torch