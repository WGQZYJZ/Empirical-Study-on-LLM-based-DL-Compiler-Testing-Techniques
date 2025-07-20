input_data = torch.randn(2, 3, 4)
module = torch.nn.Linear(4, 3)
weight_norm = torch.nn.utils.weight_norm(module)
output = weight_norm(input_data)