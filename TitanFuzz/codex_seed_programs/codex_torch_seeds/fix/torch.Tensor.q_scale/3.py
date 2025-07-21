'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.q_scale\ntorch.Tensor.q_scale(_input_tensor)\n'
import torch
input_data = torch.rand(1, 32, 32)
output = torch.Tensor.q_scale(input_data)
print(output)