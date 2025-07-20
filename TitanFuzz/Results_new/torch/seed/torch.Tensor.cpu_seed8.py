_input_tensor = torch.randn(2, 3, 4, 5)
_out_tensor = torch.Tensor.cpu(_input_tensor, memory_format=torch.preserve_format)