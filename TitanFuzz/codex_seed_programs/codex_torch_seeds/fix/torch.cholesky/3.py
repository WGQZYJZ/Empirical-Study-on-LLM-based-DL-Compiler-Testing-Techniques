'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cholesky\ntorch.cholesky(input, upper=False, *, out=None)\n'
import torch
input_data = torch.Tensor([[4, 12, (- 16)], [12, 37, (- 43)], [(- 16), (- 43), 98]])
torch.cholesky(input_data)