'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.q_scale\ntorch.Tensor.q_scale(_input_tensor)\n'
import torch
input_tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
print(('input_tensor = ' + str(input_tensor)))
q_scale = input_tensor.q_scale()
print(('q_scale = ' + str(q_scale)))