'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.q_zero_point\ntorch.Tensor.q_zero_point(_input_tensor)\n'
import torch
input_tensor = torch.rand(1, 3, 4, 4).cuda().half()
output = torch.Tensor.q_zero_point(input_tensor)
print(output)