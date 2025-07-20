vec = torch.rand(10)
parameters = nn.ParameterList([nn.Parameter(torch.rand(10))])
torch.nn.utils.vector_to_parameters(vec, parameters)