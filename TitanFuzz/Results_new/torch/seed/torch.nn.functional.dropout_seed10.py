input_data = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
output_data = torch.nn.functional.dropout(input_data, p=0.5, training=True, inplace=False)
input_data = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])