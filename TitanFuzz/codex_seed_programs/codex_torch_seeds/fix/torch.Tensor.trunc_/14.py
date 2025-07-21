'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.trunc_\ntorch.Tensor.trunc_(_input_tensor)\n'
import torch
input_tensor = torch.tensor([(- 1.2), (- 2.3), (- 3.4), (- 4.5), (- 5.6), (- 6.7), (- 7.8), (- 8.9), (- 9.0)])
output_tensor = input_tensor.trunc_()
print('input data:', input_tensor)
print('output data:', output_tensor)