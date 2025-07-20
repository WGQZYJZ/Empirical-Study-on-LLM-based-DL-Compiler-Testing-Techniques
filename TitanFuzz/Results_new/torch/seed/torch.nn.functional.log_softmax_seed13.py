input_data = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]], dtype=torch.float)
torch.nn.functional.log_softmax(input_data, dim=1)
input_data = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]], dtype=torch.float)
torch.nn.functional.softmax(input_data, dim=1)
input_data