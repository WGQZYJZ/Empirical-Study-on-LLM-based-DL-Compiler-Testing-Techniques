'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.rot90\ntorch.Tensor.rot90(_input_tensor, k, dims)\n'
import torch
input_tensor = torch.randint(low=0, high=9, size=(2, 3, 4, 5), dtype=torch.float32)
print('Input tensor:')
print(input_tensor)
output_tensor = input_tensor.rot90(k=2, dims=(2, 3))
print('Output tensor:')
print(output_tensor)