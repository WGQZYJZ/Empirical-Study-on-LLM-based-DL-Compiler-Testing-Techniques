'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.quantize_per_tensor\ntorch.quantize_per_tensor(input, scale, zero_point, dtype)\n'
import torch
import numpy as np
import torch
input = torch.rand((1, 3, 224, 224))
output = torch.quantize_per_tensor(input, scale=1.0, zero_point=0, dtype=torch.quint8)
print(output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.quantize_per_channel\ntorch.quantize_per_channel(input, scales, zero_points, axis, dtype)\n'
import torch
import numpy as np
import torch
input = torch.rand((1, 3, 224, 224))