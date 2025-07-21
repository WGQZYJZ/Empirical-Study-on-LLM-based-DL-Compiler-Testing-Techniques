'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.byte\ntorch.Tensor.byte(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
_input_tensor = torch.randint(low=0, high=255, size=(10, 10), dtype=torch.uint8)
_output_tensor = _input_tensor.byte()
print('Input tensor:', _input_tensor)
print('Output tensor:', _output_tensor)