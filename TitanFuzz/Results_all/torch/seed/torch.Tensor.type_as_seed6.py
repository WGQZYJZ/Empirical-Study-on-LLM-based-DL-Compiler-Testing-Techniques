input_tensor = torch.rand(2, 3)
output_tensor = torch.Tensor.type_as(input_tensor, torch.IntTensor())