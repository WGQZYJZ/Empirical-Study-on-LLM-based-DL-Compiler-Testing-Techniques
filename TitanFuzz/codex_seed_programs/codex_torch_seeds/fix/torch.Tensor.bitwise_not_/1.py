'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_not_\ntorch.Tensor.bitwise_not_(_input_tensor)\n'
import torch
input_tensor = torch.tensor([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=torch.bool)
output_tensor = torch.Tensor.bitwise_not_(input_tensor)
print(output_tensor)