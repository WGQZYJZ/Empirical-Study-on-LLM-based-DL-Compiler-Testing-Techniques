'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.q_zero_point\ntorch.Tensor.q_zero_point(_input_tensor)\n'
import torch
_input_tensor = torch.rand(2, 3, 4)
_output_tensor = _input_tensor.q_zero_point()
print('The input tensor is: ', _input_tensor)
print('The output tensor is: ', _output_tensor)