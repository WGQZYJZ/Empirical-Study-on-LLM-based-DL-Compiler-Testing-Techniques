'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sparse.mm\ntorch.sparse.mm(mat1, mat2)\n'
import torch
import torch
i = torch.tensor([[0, 1, 1], [2, 0, 2]])
v = torch.tensor([3, 4, 5], dtype=torch.float32)
shape = torch.Size([3, 3])
mat1 = torch.sparse_coo_tensor(i, v, shape)
i = torch.tensor([[0, 1, 1], [2, 0, 2]])
v = torch.tensor([1, 2, 3], dtype=torch.float32)
shape = torch.Size([3, 3])
mat2 = torch.sparse_coo_tensor(i, v, shape)
result = torch.sparse.mm(mat1, mat2)
print(result)