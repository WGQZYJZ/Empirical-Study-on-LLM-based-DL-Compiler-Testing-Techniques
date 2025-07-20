input_tensor = torch.arange(start=0, end=24, dtype=torch.float32).reshape(2, 3, 4)
split_tensor_list = torch.Tensor.dsplit(input_tensor, split_size_or_sections=2)