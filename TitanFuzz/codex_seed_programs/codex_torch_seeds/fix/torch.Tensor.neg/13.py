'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.neg\ntorch.Tensor.neg(_input_tensor)\n'
import torch
input_tensor = torch.randint(low=0, high=10, size=(5, 5), dtype=torch.float32)
print('Input tensor:\n{}'.format(input_tensor))
neg_tensor = torch.Tensor.neg(input_tensor)
print('Negative tensor:\n{}'.format(neg_tensor))