'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.equal\ntorch.Tensor.equal(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.float32)
output_tensor = torch.Tensor.equal(input_tensor, torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.float32))
print('The input tensor is:', input_tensor)
print('The output tensor is:', output_tensor)