'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.q_scale\ntorch.Tensor.q_scale(_input_tensor)\n'
import torch
import torch.nn as nn
_input_tensor = torch.randint(low=0, high=256, size=(1, 3, 224, 224), dtype=torch.uint8)
_output_tensor = _input_tensor.q_scale()
print(_output_tensor)