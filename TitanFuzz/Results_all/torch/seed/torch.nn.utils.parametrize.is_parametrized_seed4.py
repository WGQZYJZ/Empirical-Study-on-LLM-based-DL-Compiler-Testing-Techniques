module = torch.nn.Linear(2, 3)
tensor_name = 'weight'
is_parametrized = torch.nn.utils.parametrize.is_parametrized(module, tensor_name)