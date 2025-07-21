'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.addcmul\ntorch.addcmul(input, tensor1, tensor2, *, value=1, out=None)\n'
import torch
t1 = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
t2 = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
t3 = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
torch.addcmul(t1, t2, t3)
print(t1)