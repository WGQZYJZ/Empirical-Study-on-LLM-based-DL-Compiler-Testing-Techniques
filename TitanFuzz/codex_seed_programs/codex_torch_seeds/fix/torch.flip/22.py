'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.flip\ntorch.flip(input, dims)\n'
import torch
import numpy as np
input_data = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print('Input data: {}'.format(input_data))
input_data = torch.from_numpy(input_data)
print('Input data: {}'.format(input_data))
output_data = torch.flip(input_data, [0])
print('Output data: {}'.format(output_data))