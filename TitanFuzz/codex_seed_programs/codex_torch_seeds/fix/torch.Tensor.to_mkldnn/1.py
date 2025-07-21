'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.to_mkldnn\ntorch.Tensor.to_mkldnn(_input_tensor)\n'
import torch
import numpy as np
input_tensor = torch.randn(1, 3, 224, 224)
output_tensor = input_tensor.to_mkldnn()
print(output_tensor)