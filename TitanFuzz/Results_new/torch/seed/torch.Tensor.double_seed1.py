_input_tensor = torch.randn(1, 2, 3, 4)
_input_tensor = torch.Tensor.double(_input_tensor, memory_format=torch.preserve_format)
_input_tensor = torch.randn(1, 2, 3, 4)
_input_tensor = torch.Tensor.float(_input_tensor, memory_format=torch.preserve_format)