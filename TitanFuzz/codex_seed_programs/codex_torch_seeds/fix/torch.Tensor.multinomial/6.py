'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.multinomial\ntorch.Tensor.multinomial(_input_tensor, num_samples, replacement=False, *, generator=None)\n'
import torch
_input_tensor = torch.Tensor([[0.1, 0.2, 0.3, 0.4], [0.2, 0.3, 0.4, 0.5], [0.3, 0.4, 0.5, 0.6]])
_output_tensor = torch.Tensor.multinomial(_input_tensor, 2, replacement=True)
print('input tensor: \n', _input_tensor)
print('output tensor: \n', _output_tensor)