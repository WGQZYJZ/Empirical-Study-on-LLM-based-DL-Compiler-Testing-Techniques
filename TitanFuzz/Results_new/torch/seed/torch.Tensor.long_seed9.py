_input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
_output_tensor = torch.Tensor.long(_input_tensor, memory_format=torch.preserve_format)