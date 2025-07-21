'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cumsum\ntorch.cumsum(input, dim, *, dtype=None, out=None)\n'
import torch
input = torch.randn(2, 3, 4)
print(f'''input = 
{input}''')
output = torch.cumsum(input, dim=0)
print(f'''output = 
{output}''')
output = torch.cumsum(input, dim=1)
print(f'''output = 
{output}''')
output = torch.cumsum(input, dim=2)
print(f'''output = 
{output}''')