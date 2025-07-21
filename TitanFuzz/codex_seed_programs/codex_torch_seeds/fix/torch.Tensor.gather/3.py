'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.gather\ntorch.Tensor.gather(_input_tensor, dim, index)\n'
import torch
'\nimport PyTorch\n'
'\nGenerate input data\n'
input_tensor = torch.rand(3, 4)
print(input_tensor)
'\nCall the API torch.Tensor.gather\ntorch.Tensor.gather(_input_tensor, dim, index)\n'
output_tensor = input_tensor.gather(1, torch.tensor([[0, 0], [1, 1], [2, 2]]))
print(output_tensor)