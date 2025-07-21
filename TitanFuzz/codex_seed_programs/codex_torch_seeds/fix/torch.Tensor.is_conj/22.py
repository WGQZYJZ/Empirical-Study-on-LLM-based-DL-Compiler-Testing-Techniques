'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_conj\ntorch.Tensor.is_conj(_input_tensor)\n'
import torch
input_tensor = torch.randint(low=0, high=10, size=(5, 5), dtype=torch.float32)
output_tensor = input_tensor.is_conj()
print('input_tensor: ', input_tensor)
print('output_tensor: ', output_tensor)