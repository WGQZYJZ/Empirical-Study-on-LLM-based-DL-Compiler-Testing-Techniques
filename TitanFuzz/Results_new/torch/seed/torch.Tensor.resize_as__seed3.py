input_tensor = torch.rand(2, 3, 4, 5)
torch.Tensor.resize_as_(input_tensor, input_tensor, memory_format=torch.contiguous_format)