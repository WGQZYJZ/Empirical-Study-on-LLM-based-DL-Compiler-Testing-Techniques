'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.heaviside\ntorch.Tensor.heaviside(_input_tensor, values)\n'
import torch
input_tensor = torch.tensor([[(- 1), 0, 1], [2, 3, 4]], dtype=torch.float32)
print(torch.Tensor.heaviside(input_tensor, 0.5))
'\nTask 4: Call the API torch.Tensor.heaviside\ntorch.Tensor.heaviside(_input_tensor, values)\n'
import torch
input_tensor = torch.tensor([[(- 1), 0, 1], [2, 3, 4]], dtype=torch.float32)
print(torch.Tensor.heaviside(input_tensor, torch.tensor([[0.5, 0.5, 0.5], [0.5, 0.5, 0.5]], dtype=torch.float32)))
'\nTask 5: Call the API torch.Tensor.heaviside\ntorch.Tensor.heaviside(_input_tensor, values)\n'
import torch