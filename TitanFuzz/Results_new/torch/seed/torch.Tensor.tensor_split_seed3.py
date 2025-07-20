input_tensor = torch.arange(start=0, end=12, step=1, dtype=torch.float32)
input_tensor = input_tensor.reshape(3, 4)
indices_or_sections = [1, 2]
output_tensor_list = torch.Tensor.tensor_split(input_tensor, indices_or_sections, dim=0)
indices_or_sections = [2, 1]
output_tensor_list = torch.Tensor.tensor_split