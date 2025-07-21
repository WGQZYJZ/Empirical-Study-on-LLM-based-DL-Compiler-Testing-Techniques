'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ParameterDict\ntorch.nn.ParameterDict(parameters=None)\n'
import torch
input_data = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
param_dict = torch.nn.ParameterDict(parameters=None)
print('The type of param_dict: ', type(param_dict))
print('The content of param_dict: ', param_dict)
param_dict.update({'param1': torch.nn.Parameter(input_data)})
param_dict.update({'param2': torch.nn.Parameter(input_data)})
print('The content of param_dict after adding parameters: ', param_dict)
print('The first parameter in param_dict: ', param_dict['param1'])
print('The second parameter in param_dict: ', param_dict['param2'])
del param_dict['param1']
print