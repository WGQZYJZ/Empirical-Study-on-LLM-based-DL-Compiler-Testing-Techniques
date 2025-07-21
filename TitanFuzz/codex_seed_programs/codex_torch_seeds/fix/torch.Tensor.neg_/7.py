'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.neg_\ntorch.Tensor.neg_(_input_tensor)\n'
import torch
data = torch.tensor([(- 1), (- 2), (- 3), (- 4)])
torch.Tensor.neg_(data)
print('Negative of data: ', data)