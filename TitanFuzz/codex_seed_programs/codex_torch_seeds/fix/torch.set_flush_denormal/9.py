'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_flush_denormal\ntorch.set_flush_denormal(mode)\n'
import torch
import numpy as np
input_data = np.random.randn(3, 3).astype(np.float32)
print('Input data: \n', input_data)
torch.set_flush_denormal(True)
input_data = torch.from_numpy(input_data)
print('Convert numpy array to tensor: \n', input_data)
output_data = input_data.numpy()
print('Convert tensor to numpy array: \n', output_data)