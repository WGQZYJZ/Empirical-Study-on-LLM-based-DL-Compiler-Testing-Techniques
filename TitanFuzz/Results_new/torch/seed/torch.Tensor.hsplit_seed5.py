input_tensor = torch.arange(0, 16, dtype=torch.float32).view(2, 8)
output_tensor_list = torch.Tensor.hsplit(input_tensor, split_size_or_sections=4)
for (i, tensor) in enumerate(output_tensor_list):
    print(('output_tensor_list[%d]:' % i), tensor)