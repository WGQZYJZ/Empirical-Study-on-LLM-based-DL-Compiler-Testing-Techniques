input_tensor = torch.rand(2, 3, 4)
output_tensor = torch.Tensor.as_subclass(input_tensor, torch.FloatTensor)