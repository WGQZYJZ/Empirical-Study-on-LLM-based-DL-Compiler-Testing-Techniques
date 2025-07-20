input_data = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
param_dict = torch.nn.ParameterDict(parameters=None)
param_dict.update({'param1': torch.nn.Parameter(input_data)})
param_dict.update({'param2': torch.nn.Parameter(input_data)})
del param_dict['param1']