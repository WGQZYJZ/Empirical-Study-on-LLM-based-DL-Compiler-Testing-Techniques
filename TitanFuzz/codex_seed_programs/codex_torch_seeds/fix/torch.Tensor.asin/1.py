'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.asin\ntorch.Tensor.asin(_input_tensor)\n'
import torch
import numpy as np
import torch
import numpy as np
input_tensor = torch.randn(3, 5)
print(input_tensor)
output_tensor = input_tensor.asin()
print(output_tensor)
print(np.arcsin(input_tensor.numpy()))