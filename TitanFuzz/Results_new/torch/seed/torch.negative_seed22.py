input_data = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
output_data = torch.negative(input=input_data)
output_data = torch.tensor([[0, 0, 0], [0, 0, 0]], dtype=torch.float32)
torch.negative(input=input_data, out=output_data)