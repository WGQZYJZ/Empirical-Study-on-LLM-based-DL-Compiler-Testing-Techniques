input_data = torch.ones(2, 3)
output_data = torch.ones(2, 3)
if torch.equal(input_data, output_data):
    print('The input and output data are the same.')
else:
    print('The input and output data are different.')