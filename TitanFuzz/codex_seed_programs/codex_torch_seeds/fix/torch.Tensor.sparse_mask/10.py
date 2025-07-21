'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sparse_mask\ntorch.Tensor.sparse_mask(_input_tensor, mask)\n'
import torch
input_tensor = torch.Tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
mask = torch.Tensor([[0, 0, 1, 0], [0, 0, 0, 0], [1, 0, 0, 0]])
output_tensor = input_tensor.sparse_mask(mask)
print('The input tensor is: ', input_tensor)
print('The mask is: ', mask)
print('The output tensor is: ', output_tensor)