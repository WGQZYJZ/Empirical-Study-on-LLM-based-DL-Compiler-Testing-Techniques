_input_tensor = torch.rand(2, 3, 3, 3)
torch.Tensor.int(_input_tensor, memory_format=torch.preserve_format)