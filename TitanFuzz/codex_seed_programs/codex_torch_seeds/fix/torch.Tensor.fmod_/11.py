'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.fmod_\ntorch.Tensor.fmod_(_input_tensor, divisor)\n'
import torch
input_tensor = torch.tensor([(- 3.1415), (- 3.1415), (- 3.1415), (- 3.1415)])
torch.Tensor.fmod_(input_tensor, 3.1415)
print(input_tensor)