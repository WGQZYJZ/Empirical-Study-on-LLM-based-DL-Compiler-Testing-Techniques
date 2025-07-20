input_data = torch.arange((- 5), 5, 0.1)
input_data = input_data.view(input_data.size(0), 1)
prelu = torch.nn.PReLU(num_parameters=1, init=0.25)
output = prelu(input_data)