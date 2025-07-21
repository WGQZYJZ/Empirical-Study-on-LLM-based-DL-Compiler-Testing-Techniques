'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.amin\ntorch.Tensor.amin(_input_tensor, dim=None, keepdim=False)\n'
import torch
import torch
input_tensor = torch.rand(2, 3, 4)
print('Input tensor: \n', input_tensor)
print('Minimum value of input tensor: ', input_tensor.amin())
print('Minimum value of input tensor along dimension 0: ', input_tensor.amin(dim=0))
print('Minimum value of input tensor along dimension 1: ', input_tensor.amin(dim=1))
print('Minimum value of input tensor along dimension 2: ', input_tensor.amin(dim=2))
print('Minimum value of input tensor along dimension 0, keepdim=True: ', input_tensor.amin(dim=0, keepdim=True))
print('Minimum value of input tensor along dimension 1, keepdim=True: ', input_tensor.amin(dim=1, keepdim=True))