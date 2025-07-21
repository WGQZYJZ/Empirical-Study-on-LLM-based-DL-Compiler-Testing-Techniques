'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sign_\ntorch.Tensor.sign_(_input_tensor)\n'
import torch
input_tensor = torch.tensor([(- 1.0), (- 0.5), 0.0, 0.5, 1.0])
print(input_tensor.sign_())