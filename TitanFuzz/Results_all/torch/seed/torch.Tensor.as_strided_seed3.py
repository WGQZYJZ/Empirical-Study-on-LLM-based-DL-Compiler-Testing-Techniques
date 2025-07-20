_input_tensor = torch.randn(3, 3)
_strided_tensor = torch.Tensor.as_strided(_input_tensor, (3, 2), (2, 2))