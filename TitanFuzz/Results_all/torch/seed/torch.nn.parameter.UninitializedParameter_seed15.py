input_data = torch.rand(1, 5)
weight = torch.nn.parameter.UninitializedParameter(requires_grad=True, device=None, dtype=None)
weight = torch.nn.parameter.Parameter(torch.rand(1, 5))
weight = torch.nn.parameter.Parameter(torch.rand(1, 5))
weight = torch.nn.parameter.Parameter(torch.rand(1, 5))
weight = torch.nn.parameter.Parameter(torch.rand(1, 5))