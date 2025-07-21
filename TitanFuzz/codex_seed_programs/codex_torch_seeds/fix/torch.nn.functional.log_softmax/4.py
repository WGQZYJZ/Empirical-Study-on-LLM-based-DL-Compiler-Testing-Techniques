'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.log_softmax\ntorch.nn.functional.log_softmax(input, dim=None, _stacklevel=3, dtype=None)\n'
import torch
import numpy as np
input_data = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
output_data = torch.nn.functional.log_softmax(input_data, dim=1)
print(output_data)