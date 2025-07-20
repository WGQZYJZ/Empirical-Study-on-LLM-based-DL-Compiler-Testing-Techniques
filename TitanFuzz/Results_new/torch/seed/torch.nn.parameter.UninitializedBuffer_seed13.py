input_data = torch.randn(2, 3)
uninitialized_buffer = torch.nn.parameter.UninitializedBuffer(requires_grad=False, device=None, dtype=None)