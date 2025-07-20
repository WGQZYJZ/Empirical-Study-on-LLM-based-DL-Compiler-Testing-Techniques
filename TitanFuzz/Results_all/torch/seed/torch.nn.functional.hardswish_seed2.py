if True:
    input_data = torch.tensor(np.array([[(- 1), (- 0.5), 0, 0.5, 1]]), dtype=torch.float)
    print('Input data: \n{}'.format(input_data))
    output_data = torch.nn.functional.hardswish(input_data, inplace=False)
    print('Output data: \n{}'.format(output_data))