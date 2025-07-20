input_tensor = torch.rand(1, 3, 224, 224)
output_tensor = torch.Tensor.type_as(input_tensor, torch.float16)