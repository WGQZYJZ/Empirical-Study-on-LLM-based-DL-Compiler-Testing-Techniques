'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.log_normal_\ntorch.Tensor.log_normal_(_input_tensor, mean=1, std=2, *, generator=None\n'
import torch
_input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
_output_tensor = torch.Tensor.log_normal_(_input_tensor, mean=1, std=2)
print('The result of task 3 is: ', _output_tensor)
print('The type of the result of task 3 is: ', type(_output_tensor))