'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.byte\ntorch.Tensor.byte(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
_input_tensor = torch.randint(0, 255, (1, 3, 3, 3), dtype=torch.uint8)
_output_tensor = torch.Tensor.byte(_input_tensor, memory_format=torch.preserve_format)
print(_output_tensor)