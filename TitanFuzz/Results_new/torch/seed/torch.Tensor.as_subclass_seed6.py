input_tensor = torch.randn(3, 3)
output_tensor = torch.Tensor.as_subclass(input_tensor, torch.FloatTensor)