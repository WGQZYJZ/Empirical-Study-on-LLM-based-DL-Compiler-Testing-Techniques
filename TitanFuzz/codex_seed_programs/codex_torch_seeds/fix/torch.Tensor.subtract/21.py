'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.subtract\ntorch.Tensor.subtract(_input_tensor, other, *, alpha=1)\n'
import torch
input_tensor = torch.randn(3, 3)
other_tensor = torch.randn(3, 3)
print(f'''input_tensor: 
{input_tensor}''')
print(f'''other_tensor: 
{other_tensor}''')
output_tensor = input_tensor.subtract(other_tensor)
print(f'''output_tensor: 
{output_tensor}''')