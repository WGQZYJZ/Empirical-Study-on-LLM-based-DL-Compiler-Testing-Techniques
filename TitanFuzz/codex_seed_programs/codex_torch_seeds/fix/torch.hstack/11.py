'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.hstack\ntorch.hstack(tensors, *, out=None)\n'
import torch
input_tensors = []
for i in range(3):
    input_tensors.append(torch.randn(2, 2))
output_tensor = torch.hstack(input_tensors)
print('The size of output tensor: ', output_tensor.size())
print('The value of output tensor: \n', output_tensor)