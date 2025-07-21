'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.byte\ntorch.Tensor.byte(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
_input_tensor = torch.randint(1, 10, (3, 3), dtype=torch.float32)
print('Input Tensor: ', _input_tensor)
_output_tensor = torch.Tensor.byte(_input_tensor)
print('Output Tensor: ', _output_tensor)