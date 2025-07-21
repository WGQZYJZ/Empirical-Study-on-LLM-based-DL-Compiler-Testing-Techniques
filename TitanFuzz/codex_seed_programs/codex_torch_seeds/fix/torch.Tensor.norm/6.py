"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.norm\ntorch.Tensor.norm(_input_tensor, p='fro', dim=None, keepdim=False, dtype=None)\n"
import torch
'\nimport PyTorch\n'
'\nGenerate input data\n'
_input_tensor = torch.tensor([[1, 2], [3, 4]])
'\nCall the API torch.Tensor.norm\n'
_output_tensor = _input_tensor.norm()
print(_output_tensor)