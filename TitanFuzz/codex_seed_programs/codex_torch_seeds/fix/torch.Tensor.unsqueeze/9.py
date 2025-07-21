'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.unsqueeze\ntorch.Tensor.unsqueeze(_input_tensor, dim)\n'
import torch
tensor_1d = torch.arange(0, 10)
print('tensor_1d: ', tensor_1d)
tensor_2d = tensor_1d.unsqueeze(0)
print('tensor_2d: ', tensor_2d)
tensor_3d = tensor_1d.unsqueeze(1)
print('tensor_3d: ', tensor_3d)