_input_tensor = torch.randn(2, 3, 4, 5, 6)
torch.Tensor.long(_input_tensor, memory_format=torch.preserve_format)