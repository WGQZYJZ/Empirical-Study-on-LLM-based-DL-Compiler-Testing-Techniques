'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ParameterDict\ntorch.nn.ParameterDict(parameters=None)\n'
import torch
input_data = {'param1': torch.randn(2, 3), 'param2': torch.randn(2, 3)}
parameter_dict = torch.nn.ParameterDict(parameters=input_data)
print('The input data is: ', input_data)
print('The type of input data is: ', type(input_data))
print('The output data is: ', parameter_dict)
print('The type of output data is: ', type(parameter_dict))