input_data = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float)
prelu = torch.nn.PReLU(num_parameters=1, init=0.25)
output = prelu(input_data)