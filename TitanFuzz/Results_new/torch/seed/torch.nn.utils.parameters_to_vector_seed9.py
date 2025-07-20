a = torch.randn(5, requires_grad=True)
b = torch.randn(5, requires_grad=True)
c = torch.randn(5, requires_grad=True)
param_vector = torch.nn.utils.parameters_to_vector([a, b, c])