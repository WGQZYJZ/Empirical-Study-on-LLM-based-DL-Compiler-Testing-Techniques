'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logit\ntorch.Tensor.logit(_input_tensor)\n'
import torch
input_data = torch.randint(low=0, high=2, size=(5, 5), dtype=torch.int8)
print('Input data: ', input_data)
logit_output = torch.Tensor.logit(input_data)
print('Output: ', logit_output)