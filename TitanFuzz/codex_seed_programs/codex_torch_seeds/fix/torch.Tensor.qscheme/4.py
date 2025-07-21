'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.qscheme\ntorch.Tensor.qscheme(_input_tensor)\n'
import torch
_input_tensor = torch.randint(low=0, high=256, size=(2, 3, 4, 4), dtype=torch.uint8)
print(_input_tensor.qscheme())