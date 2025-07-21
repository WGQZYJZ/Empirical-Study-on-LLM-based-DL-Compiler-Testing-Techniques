'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.q_zero_point\ntorch.Tensor.q_zero_point(_input_tensor)\n'
import torch
input_tensor = torch.rand(5, 5, dtype=torch.float32)
print('Input tensor: ', input_tensor)
q_zero_point = input_tensor.q_zero_point()
print('Quantized zero point of input tensor: ', q_zero_point)