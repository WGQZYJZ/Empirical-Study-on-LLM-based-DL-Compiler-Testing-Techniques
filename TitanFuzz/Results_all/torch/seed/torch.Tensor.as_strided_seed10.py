_input_tensor = torch.arange(0, 9, dtype=torch.float32).view(3, 3)
size = [4, 2]
stride = [2, 1]
output_tensor = torch.Tensor.as_strided(_input_tensor, size, stride)