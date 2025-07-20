_input_tensor = torch.randn(3, 3, requires_grad=True)
_cpu_tensor = torch.Tensor.cpu(_input_tensor, memory_format=torch.preserve_format)