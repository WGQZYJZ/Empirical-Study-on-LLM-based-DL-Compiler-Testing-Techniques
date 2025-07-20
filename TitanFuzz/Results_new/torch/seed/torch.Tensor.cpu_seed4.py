_input_tensor = torch.rand(2, 3, 4, 5, 6)
torch.Tensor.cpu(_input_tensor, memory_format=torch.preserve_format)