_input_tensor = torch.randn(2, 3, 4, 5)
torch.Tensor.contiguous(_input_tensor, memory_format=torch.contiguous_format)