'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cuda\ntorch.Tensor.cuda(_input_tensor, device=None, non_blocking=False, memory_format=torch.preserve_format)\n'
import torch
input_tensor = torch.randn(2, 3, 4)
output_tensor = input_tensor.cuda()
print('input_tensor:', input_tensor)
print('output_tensor:', output_tensor)