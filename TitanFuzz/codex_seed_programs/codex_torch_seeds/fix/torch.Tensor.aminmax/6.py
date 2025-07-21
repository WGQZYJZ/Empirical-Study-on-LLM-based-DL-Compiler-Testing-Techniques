'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.aminmax\ntorch.Tensor.aminmax(_input_tensor, *, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randint(1, 10, (2, 3))
print('Input:')
print(input_tensor)
output_tensor = input_tensor.aminmax(dim=1, keepdim=True)
print('Output:')
print(output_tensor)