'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.long\ntorch.Tensor.long(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
_input_tensor = torch.randint(low=0, high=100, size=(4, 4))
_output_tensor = _input_tensor.long()
print(_input_tensor)
print(_output_tensor)
print(type(_input_tensor))
print(type(_output_tensor))
'\nTask 4: Call the API torch.Tensor.long\ntorch.Tensor.long(_input_tensor, memory_format=torch.channels_last)\n'
_input_tensor = torch.randint(low=0, high=100, size=(4, 4))
_output_tensor = _input_tensor.long(memory_format=torch.channels_last)
print(_input_tensor)
print(_output_tensor)
print(type(_input_tensor))
print(type(_output_tensor))