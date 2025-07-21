'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.device\ntorch.Tensor.device(_input_tensor, )\n'
import torch
input_tensor = torch.randn(5, 3)
device = torch.Tensor.device(input_tensor)
print('device: ', device)