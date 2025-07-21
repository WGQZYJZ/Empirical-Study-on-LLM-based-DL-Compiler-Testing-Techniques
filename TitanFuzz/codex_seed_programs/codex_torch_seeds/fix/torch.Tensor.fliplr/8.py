'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.fliplr\ntorch.Tensor.fliplr(_input_tensor)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3, 4], [4, 3, 2, 1]])
print('Original input tensor:')
print(input_tensor)
import torch
input_tensor = torch.tensor([[1, 2, 3, 4], [4, 3, 2, 1]])
output_tensor = torch.Tensor.fliplr(input_tensor)
print('Output tensor:')
print(output_tensor)