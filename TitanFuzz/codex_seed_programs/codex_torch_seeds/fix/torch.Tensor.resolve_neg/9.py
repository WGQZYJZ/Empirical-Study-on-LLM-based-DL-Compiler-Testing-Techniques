'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.resolve_neg\ntorch.Tensor.resolve_neg(_input_tensor)\n'
import torch
import numpy as np
data = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(data)
tensor = torch.Tensor(data)
print(tensor)
print(tensor.resolve_neg())
'\nExpected output:\n[[1. 2. 3. 4.]\n [5. 6. 7. 8.]\n [9. 10. 11. 12.]]\ntensor([[ 1.,  2.,  3.,  4.],\n        [ 5.,  6.,  7.,  8.],\n        [ 9., 10., 11., 12.]])\ntensor([[ 1.,  2.,  3.,  4.],\n        [ 5.,  6.,  7.,  8.],\n        [ 9., 10., 11., 12.]])\n'