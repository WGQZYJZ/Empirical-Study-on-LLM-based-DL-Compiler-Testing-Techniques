'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.quantize_per_tensor\ntorch.quantize_per_tensor(input, scale, zero_point, dtype)\n'
import torch
import numpy as np
input_data = np.random.randn(100, 100)
input_data = input_data.astype(np.float32)
input_tensor = torch.tensor(input_data)
quantized_tensor = torch.quantize_per_tensor(input_tensor, scale=1.0, zero_point=0, dtype=torch.quint8)
print(quantized_tensor)