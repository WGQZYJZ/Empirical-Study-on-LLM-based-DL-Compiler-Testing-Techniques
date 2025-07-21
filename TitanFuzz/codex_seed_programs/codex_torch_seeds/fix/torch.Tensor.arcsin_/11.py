'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arcsin_\ntorch.Tensor.arcsin_(_input_tensor)\n'
import torch
import math
input_tensor = torch.tensor([(- 1.0), (- 0.5), 0.0, 0.5, 1.0])
arcsin_result = torch.Tensor.arcsin_(input_tensor)
print('The result of arcsin_ is: ', arcsin_result)
for i in input_tensor:
    print('The result of math.asin is: ', math.asin(i))