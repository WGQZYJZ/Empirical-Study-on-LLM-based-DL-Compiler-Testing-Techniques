gelu = torch.nn.GELU()
input_data = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
output = gelu(input_data)