'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.quantize_per_tensor\ntorch.quantize_per_tensor(input, scale, zero_point, dtype)\n'
import torch
import numpy as np
import torch
input_data = torch.rand(1, 3, 224, 224)
quantized_data = torch.quantize_per_tensor(input_data, 0.01, 0, torch.quint8)
print(quantized_data)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.quantize_per_channel\ntorch.quantize_per_channel(input, scales, zero_points, axis, dtype)\n'
import torch
import numpy as np
import torch
input_data = torch.rand(1, 3, 224, 224)