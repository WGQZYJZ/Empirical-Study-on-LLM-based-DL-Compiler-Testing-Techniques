_input_tensor = torch.randn(5, 5)
_tensor_int = torch.Tensor.int(_input_tensor, memory_format=torch.preserve_format)
_input_tensor = torch.randn(5, 5)
_tensor_long = torch.Tensor.long(_input_tensor, memory_format=torch.preserve_format)