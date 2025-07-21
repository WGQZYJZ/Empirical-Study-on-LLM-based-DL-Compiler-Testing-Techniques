'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.overrides.is_tensor_like\ntorch.overrides.is_tensor_like(inp)\n'
import torch
tensor = torch.randn(2, 2)
list_ = [[1, 2], [3, 4]]
tuple_ = (1, 2, 3, 4)
import numpy as np
numpy_array = np.array([[1, 2], [3, 4]])
python_int = 5
python_float = 5.0
python_string = 'PyTorch'
python_boolean = True
print('tensor: ', torch.overrides.is_tensor_like(tensor))
print('list: ', torch.overrides.is_tensor_like(list_))