'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sign_\ntorch.Tensor.sign_(_input_tensor)\n'
import torch
input_tensor = torch.tensor([[(- 2), (- 1), 0, 1, 2]], dtype=torch.float32)
torch.Tensor.sign_(input_tensor)
print('input_tensor:', input_tensor)