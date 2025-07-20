input_data = torch.tensor([[1.0, 2.0, 3.0, 4.0, 5.0]])
output_data = torch.special.log_softmax(input_data, dim=0)