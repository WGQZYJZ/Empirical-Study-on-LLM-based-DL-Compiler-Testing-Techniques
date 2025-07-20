input_tensor = torch.arange(0, 12)
indices_or_sections = [2, 4, 6]
result = torch.Tensor.tensor_split(input_tensor, indices_or_sections, dim=0)