'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.positive\ntorch.Tensor.positive(_input_tensor)\n'
import torch
_input_tensor = torch.tensor([(- 3), (- 1), (- 2), 0, 1, 2, 3])
print(torch.Tensor.positive(_input_tensor))