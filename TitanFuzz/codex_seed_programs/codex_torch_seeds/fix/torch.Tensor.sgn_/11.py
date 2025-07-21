'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sgn_\ntorch.Tensor.sgn_(_input_tensor)\n'
import torch
input_tensor = torch.tensor([[1, (- 1), (- 1), 1, 1], [1, (- 1), 1, (- 1), (- 1)]], dtype=torch.float32)
torch.Tensor.sgn_(input_tensor)
print(input_tensor)