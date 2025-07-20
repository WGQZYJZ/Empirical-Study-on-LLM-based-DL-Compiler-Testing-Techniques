input_tensor = torch.randn(2, 3, 4)
torch.Tensor.resize_(input_tensor, (3, 2, 4))
torch.Tensor.resize_(input_tensor, (3, 2, 4), memory_format=torch.channels_last)