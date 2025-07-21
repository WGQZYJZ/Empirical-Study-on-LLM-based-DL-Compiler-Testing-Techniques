'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addcmul_\ntorch.Tensor.addcmul_(_input_tensor, tensor1, tensor2, *, value=1)\n'
import torch
import numpy as np
np.random.seed(0)
tensor1 = torch.tensor(np.random.randint(10, size=(3, 3)))
tensor2 = torch.tensor(np.random.randint(10, size=(3, 3)))
tensor3 = torch.tensor(np.random.randint(10, size=(3, 3)))
torch.Tensor.addcmul_(tensor1, tensor2, tensor3)
print(tensor1)