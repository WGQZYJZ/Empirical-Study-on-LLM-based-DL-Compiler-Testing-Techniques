'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_signed\ntorch.Tensor.is_signed(_input_tensor)\n'
import torch
_input_tensor = torch.randint(low=0, high=100, size=(1, 2, 3), dtype=torch.int16)
_output_tensor = torch.Tensor.is_signed(_input_tensor)
print('The output tensor is: ', _output_tensor)