'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sign\ntorch.Tensor.sign(_input_tensor)\n'
import torch
input_tensor = torch.tensor([(- 1.0), 1.0, 0.0])
output_tensor = input_tensor.sign()
print(output_tensor)