'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cuda\ntorch.Tensor.cuda(_input_tensor, device=None, non_blocking=False, memory_format=torch.preserve_format)\n'
import torch
input_tensor = torch.randn(3, 3)
print('Input tensor: {}'.format(input_tensor))
cuda_tensor = input_tensor.cuda()
print('Cuda tensor: {}'.format(cuda_tensor))