input_data = torch.randn(1, 1, 3, 3)
uninitialized_parameter = torch.nn.parameter.UninitializedParameter(requires_grad=True, device=None, dtype=None)