data = torch.randn(2, 3)
module_dict = torch.nn.ModuleDict({'linear': torch.nn.Linear(3, 4), 'conv': torch.nn.Conv2d(3, 4, (3, 3))})
module_dict.update({'linear': torch.nn.Linear(3, 4), 'conv': torch.nn.Conv2d(3, 4, (3, 3))})