input_data = torch.tensor([2, 1, 0])
output_data = torch.nn.functional.one_hot(input_data, num_classes=3)
assert torch.all(torch.eq(output_data, torch.tensor([[0, 0, 1], [0, 1, 0], [1, 0, 0]]))), 'Wrong result, please check your code'
output_data = torch.nn.functional.one_hot(input_data, num_classes=4)