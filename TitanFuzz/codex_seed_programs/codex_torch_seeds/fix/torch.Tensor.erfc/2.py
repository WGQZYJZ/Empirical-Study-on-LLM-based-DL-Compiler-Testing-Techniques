'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.erfc\ntorch.Tensor.erfc(_input_tensor)\n'
import torch
input_tensor = torch.tensor([(- 100.0), (- 10.0), (- 1.0), 0.0, 1.0, 10.0, 100.0])
print('Input data: ', input_tensor)
output_tensor = input_tensor.erfc()
print('Output data: ', output_tensor)