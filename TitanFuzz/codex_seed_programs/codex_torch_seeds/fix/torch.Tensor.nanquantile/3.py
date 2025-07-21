'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nanquantile\ntorch.Tensor.nanquantile(_input_tensor, q, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.tensor([[0.2, 0.3, 0.4], [0.2, 0.3, 0.4]])
input_tensor = input_tensor.unsqueeze(0)
output_tensor = input_tensor.nanquantile(0.5, dim=2, keepdim=True)
print(output_tensor)