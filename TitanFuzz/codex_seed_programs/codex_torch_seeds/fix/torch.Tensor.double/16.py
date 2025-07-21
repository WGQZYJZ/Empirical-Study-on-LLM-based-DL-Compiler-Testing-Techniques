'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.double\ntorch.Tensor.double(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
import numpy as np
input_data = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float32)
input_tensor = torch.Tensor(input_data)
output_tensor = torch.Tensor.double(input_tensor)
print('The input tensor is: {}'.format(input_tensor))
print('The output tensor is: {}'.format(output_tensor))