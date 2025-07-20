input_tensor = torch.randn(2, 3, 4)
output_tensor_list = torch.Tensor.vsplit(input_tensor, 2)
for i in range(len(output_tensor_list)):
    print('output_tensor_list[{}]:'.format(i), output_tensor_list[i])