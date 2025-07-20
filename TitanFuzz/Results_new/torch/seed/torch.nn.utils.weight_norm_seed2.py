input = torch.randn(3, 3, requires_grad=True)
module = nn.Linear(3, 3)
module = torch.nn.utils.weight_norm(module, dim=0)
output = module(input)