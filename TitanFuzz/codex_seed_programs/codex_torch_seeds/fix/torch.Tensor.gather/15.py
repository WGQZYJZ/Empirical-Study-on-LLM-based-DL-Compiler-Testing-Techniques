'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.gather\ntorch.Tensor.gather(_input_tensor, dim, index)\n'
import torch
import torch
input_tensor = torch.tensor([[0.1, 0.2, 0.3, 0.4], [0.5, 0.6, 0.7, 0.8], [0.9, 1.0, 1.1, 1.2]])
print(input_tensor.gather(dim=0, index=torch.tensor([0, 2])))
print(input_tensor.gather(dim=1, index=torch.tensor([0, 2])))