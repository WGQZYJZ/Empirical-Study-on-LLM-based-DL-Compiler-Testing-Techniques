'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.atanh_\ntorch.Tensor.atanh_(_input_tensor, other)\n'
import torch
_input_tensor = torch.tensor([0.2, 0.4, 0.6, 0.8, 1.0])
_output_tensor = torch.Tensor.atanh_(_input_tensor)
print('The input tensor is:', _input_tensor)
print('The output tensor is:', _output_tensor)