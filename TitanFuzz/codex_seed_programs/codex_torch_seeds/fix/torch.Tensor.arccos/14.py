'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arccos\ntorch.Tensor.arccos(_input_tensor)\n'
import torch
input_tensor = torch.tensor([(- 1.0), (- 0.5), 0.0, 0.5, 1.0])
output_tensor = input_tensor.arccos()
print('input_tensor: ', input_tensor)
print('output_tensor: ', output_tensor)