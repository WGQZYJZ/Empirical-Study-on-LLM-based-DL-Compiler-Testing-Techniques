'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.as_subclass\ntorch.Tensor.as_subclass(_input_tensor, cls)\n'
import torch
_input_tensor = torch.rand(2, 3)
_output_tensor = torch.Tensor.as_subclass(_input_tensor, torch.FloatTensor)
print('The output tensor is: ', _output_tensor)