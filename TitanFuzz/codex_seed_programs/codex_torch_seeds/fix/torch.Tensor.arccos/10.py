'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arccos\ntorch.Tensor.arccos(_input_tensor)\n'
import torch
tensor_input = torch.rand(2, 3)
print(tensor_input)
arccos_result = torch.Tensor.arccos(tensor_input)
print(arccos_result)