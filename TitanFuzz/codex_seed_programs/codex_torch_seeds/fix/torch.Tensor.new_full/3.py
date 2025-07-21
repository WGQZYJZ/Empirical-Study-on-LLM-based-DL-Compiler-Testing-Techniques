'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_full\ntorch.Tensor.new_full(_input_tensor, size, fill_value, dtype=None, device=None, requires_grad=False)\n'
import torch
input_tensor = torch.randn(4, 4)
output_tensor = torch.Tensor.new_full(input_tensor, 3, fill_value=0.5)
print(output_tensor)
output_tensor = torch.Tensor.new_full(input_tensor, 3, fill_value=0.5, dtype=torch.int32)
print(output_tensor)
output_tensor = torch.Tensor.new_full(input_tensor, 3, fill_value=0.5, device=torch.device('cuda'))
print(output_tensor)