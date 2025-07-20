input_tensor = torch.randn(2, 3, 5, 5)
output_tensor = torch.Tensor()
torch.Tensor.resize_as_(output_tensor, input_tensor, memory_format=torch.contiguous_format)