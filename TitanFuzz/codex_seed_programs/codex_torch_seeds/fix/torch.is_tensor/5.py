'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_tensor\ntorch.is_tensor(obj)\n'
import torch
a = torch.tensor([1, 2, 3])
b = torch.tensor([[1, 2, 3], [4, 5, 6]])
c = torch.tensor([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
d = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
for obj in [a, b, c, d]:
    print(torch.is_tensor(obj))