'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.byte\ntorch.Tensor.byte(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
import numpy as np
import torch
_input_tensor = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
_input_tensor = torch.tensor(_input_tensor, dtype=torch.float32)
torch.Tensor.byte(_input_tensor, memory_format=torch.preserve_format)