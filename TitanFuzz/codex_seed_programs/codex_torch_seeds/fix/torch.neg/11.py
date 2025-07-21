'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.neg\ntorch.neg(input, *, out=None)\n'
import torch
input_tensor = torch.tensor([(- 1), (- 2), (- 3), (- 4)])
output_tensor = torch.neg(input_tensor)
print(output_tensor)