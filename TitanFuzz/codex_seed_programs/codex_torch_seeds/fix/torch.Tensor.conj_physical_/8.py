'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.conj_physical_\ntorch.Tensor.conj_physical_(_input_tensor)\n'
import torch
input_tensor = torch.randint(low=1, high=10, size=(2, 3), dtype=torch.float32)
print('Input Tensor: ', input_tensor)
print('\n')
output_tensor = torch.Tensor.conj_physical_(input_tensor)
print('Output Tensor: ', output_tensor)
print('\n')
print('Input Tensor: ', input_tensor)