'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.long\ntorch.Tensor.long(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
_input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
_output_tensor = torch.Tensor.long(_input_tensor, memory_format=torch.preserve_format)
print('_input_tensor: ', _input_tensor)
print('_output_tensor: ', _output_tensor)
'\n_input_tensor:  tensor([[1, 2, 3],\n        [4, 5, 6]])\n_output_tensor:  tensor([[1, 2, 3],\n        [4, 5, 6]])\n'