input_data = torch.randn(1, 2)
module_dict = torch.nn.ModuleDict({'linear': torch.nn.Linear(2, 2), 'conv': torch.nn.Conv2d(1, 1, 1)})