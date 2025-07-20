input_data = torch.randn(10, 3)
module_dict = torch.nn.ModuleDict({'linear_layer_1': torch.nn.Linear(3, 4), 'linear_layer_2': torch.nn.Linear(4, 5), 'linear_layer_3': torch.nn.Linear(5, 6)})