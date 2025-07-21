'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.asin\ntorch.Tensor.asin(_input_tensor)\n'
import torch
input_tensor = torch.tensor([(- 1.0), 0.0, 1.0])
print(input_tensor.asin())