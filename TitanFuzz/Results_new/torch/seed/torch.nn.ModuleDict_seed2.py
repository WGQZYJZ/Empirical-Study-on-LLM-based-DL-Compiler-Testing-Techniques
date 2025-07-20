input_data = torch.randn(2, 3, 4)
module_dict = torch.nn.ModuleDict({'conv1': torch.nn.Conv2d(3, 4, 3), 'conv2': torch.nn.Conv2d(4, 5, 3)})
module_dict.update({'conv3': torch.nn.Conv2d(5, 6, 3)})