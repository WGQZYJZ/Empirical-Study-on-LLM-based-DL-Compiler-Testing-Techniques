_input_tensor = torch.randn(2, 2)
_shared_tensor = torch.Tensor.is_shared(_input_tensor)