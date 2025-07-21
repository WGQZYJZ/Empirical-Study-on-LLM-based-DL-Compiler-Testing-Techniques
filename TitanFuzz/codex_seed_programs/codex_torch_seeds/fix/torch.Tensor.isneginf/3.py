'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.isneginf\ntorch.Tensor.isneginf(_input_tensor)\n'
import torch
input_tensor = torch.tensor([(- float('inf')), float('inf'), float('nan'), 0.0, 1.0, (- 1.0)])
output_tensor = input_tensor.isneginf()
print(output_tensor)