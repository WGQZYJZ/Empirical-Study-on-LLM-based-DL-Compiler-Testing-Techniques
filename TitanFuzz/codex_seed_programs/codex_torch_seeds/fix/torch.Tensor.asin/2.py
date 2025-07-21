'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.asin\ntorch.Tensor.asin(_input_tensor)\n'
import torch
import torch
input_tensor = torch.tensor([(- 1.0), (- 0.5), 0.0, 0.5, 1.0])
output_tensor = input_tensor.asin()
print('input_tensor:', input_tensor)
print('output_tensor:', output_tensor)
'\ninput_tensor: tensor([-1.0000, -0.5000,  0.0000,  0.5000,  1.0000])\noutput_tensor: tensor([-1.5708, -0.5235,  0.0000,  0.5235,  1.5708])\n'