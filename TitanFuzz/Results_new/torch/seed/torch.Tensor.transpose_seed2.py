input_tensor = torch.arange(start=0, end=9, step=1).reshape(3, 3)
output_tensor = torch.Tensor.transpose(input_tensor, dim0=0, dim1=1)