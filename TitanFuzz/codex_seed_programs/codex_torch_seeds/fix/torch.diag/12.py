'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.diag\ntorch.diag(input, diagonal=0, *, out=None)\n'
import torch
input = torch.randn(3, 3)
print('Generated input data: ', input)
torch.diag(input)
'\nTask 4: Call the API torch.diag_embed\ntorch.diag_embed(input, offset=0, dim1=-2, dim2=-1)\n'
torch.diag_embed(input)
'\nTask 5: Call the API torch.trace\ntorch.trace(input)\n'
torch.trace(input)
'\nTask 6: Call the API torch.tril\ntorch.tril(input, diagonal=0, out=None)\n'
torch.tril(input)
'\nTask 7: Call the API torch.triu\ntorch.triu(input, diagonal=0, out=None)\n'
torch.triu(input)