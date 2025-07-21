'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.take\ntorch.take(input, index)\n'
import torch
input = torch.randn(3, 4)
index = torch.tensor([0, 2])
print(torch.take(input, index))
'\nTask 4: Call the API torch.gather\ntorch.gather(input, dim, index)\n'
print(torch.gather(input, 0, index.view(1, (- 1))))
'\nTask 5: Call the API torch.index_select\ntorch.index_select(input, dim, index)\n'
print(torch.index_select(input, 0, index))
'\nTask 6: Call the API torch.masked_select\ntorch.masked_select(input, mask)\n'
mask = torch.tensor([[0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]], dtype=torch.uint8)
print(torch.masked_select(input, mask))
'\nTask 7: Call the API torch.nonzero\ntorch.nonzero(input)\n'
print