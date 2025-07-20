input_data = np.array([(- 1), (- 0.5), 0, 0.5, 1])
input_data = torch.Tensor(input_data)
output = torch.nn.functional.relu6(input_data)