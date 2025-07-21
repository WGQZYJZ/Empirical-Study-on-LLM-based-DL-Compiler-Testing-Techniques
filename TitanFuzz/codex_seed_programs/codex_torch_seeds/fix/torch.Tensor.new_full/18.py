'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_full\ntorch.Tensor.new_full(_input_tensor, size, fill_value, dtype=None, device=None, requires_grad=False)\n'
import torch
_input_tensor = torch.randn(4, 4)
output_tensor = torch.Tensor.new_full(_input_tensor, size=(2, 2), fill_value=3.0)
print('The input tensor is: ', _input_tensor)
print('The output tensor is: ', output_tensor)