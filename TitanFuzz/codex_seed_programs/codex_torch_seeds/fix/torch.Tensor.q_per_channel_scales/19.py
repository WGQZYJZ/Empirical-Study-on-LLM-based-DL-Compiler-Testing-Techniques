'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.q_per_channel_scales\ntorch.Tensor.q_per_channel_scales(_input_tensor)\n'
import torch
import torch.quantization
import torch.nn as nn
import torch.nn.functional as F
import torch.utils.model_zoo as model_zoo
import torch
print('Task 1: import PyTorch')
input_tensor = torch.rand(2, 3, 4, 4)
print('Task 2: Generate input data')
torch.Tensor.q_per_channel_scales(input_tensor)
print('Task 3: Call the API torch.Tensor.q_per_channel_scales')
print('torch.Tensor.q_per_channel_scales(input_tensor) = ', torch.Tensor.q_per_channel_scales(input_tensor))