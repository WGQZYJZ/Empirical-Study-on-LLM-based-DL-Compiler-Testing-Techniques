input_data = torch.randn(10, requires_grad=True)
uninitialized_parameter = torch.nn.parameter.UninitializedParameter(requires_grad=True, device=None, dtype=None)