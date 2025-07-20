input_tensor = torch.arange(start=0, end=24, out=torch.FloatTensor())
input_tensor = input_tensor.view(3, 4, 2)
output_tensor = torch.Tensor.vsplit(input_tensor, split_size_or_sections=2)