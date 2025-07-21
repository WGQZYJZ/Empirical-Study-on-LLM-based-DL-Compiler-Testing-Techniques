'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReplicationPad2d\ntorch.nn.ReplicationPad2d(padding)\n'
import torch
import numpy as np
from PIL import Image
from torchvision import transforms
import torch
input_data = torch.randn(1, 1, 4, 4)
print('input_data: ', input_data)
padding = (1, 1, 1, 1)
output_data = torch.nn.ReplicationPad2d(padding)(input_data)
print('output_data: ', output_data)