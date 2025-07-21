'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arctan_\ntorch.Tensor.arctan_(_input_tensor)\n'
import torch
input_data = torch.tensor([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0])
torch.Tensor.arctan_(input_data)
print('Arctan of input data is: ', input_data)