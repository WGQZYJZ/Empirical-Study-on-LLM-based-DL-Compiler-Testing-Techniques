input_tensor = torch.rand(2, 3, 4, 5)
tensor = torch.rand(3, 4, 5)
torch.Tensor.resize_as_(input_tensor, tensor, memory_format=torch.contiguous_format)