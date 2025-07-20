input_tensor = torch.rand(size=(2, 3))
output_tensor = torch.Tensor.transpose(input_tensor, dim0=0, dim1=1)