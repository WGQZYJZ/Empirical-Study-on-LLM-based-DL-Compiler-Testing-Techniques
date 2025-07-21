'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.byte\ntorch.Tensor.byte(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
_input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6]])
_output_tensor = torch.Tensor.byte(_input_tensor)
print(_output_tensor)