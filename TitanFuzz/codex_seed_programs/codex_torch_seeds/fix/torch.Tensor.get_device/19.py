'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.get_device\ntorch.Tensor.get_device(_input_tensor)\n'
import torch
import numpy as np
input_tensor = torch.randn(1, 3, 224, 224)
device = input_tensor.get_device()
print(device)