input_tensor = torch.rand(2, 3, 4, 5)
torch.Tensor.cpu(input_tensor, memory_format=torch.preserve_format)