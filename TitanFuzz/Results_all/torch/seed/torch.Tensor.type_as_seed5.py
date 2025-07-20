_input_tensor = torch.randn(4, 4)
torch.Tensor.type_as(_input_tensor, torch.FloatTensor)
torch.Tensor.type_as(_input_tensor, torch.DoubleTensor)
torch.Tensor.type_as(_input_tensor, torch.IntTensor)