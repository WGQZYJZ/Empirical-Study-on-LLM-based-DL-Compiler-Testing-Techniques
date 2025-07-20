input = torch.tensor([[0, 1, 2, 3], [1, 2, 3, 4]])
output = torch.nn.functional.one_hot(input, num_classes=(- 1))
input = torch.tensor([[0, 1, 2, 3], [1, 2, 3, 4]])
output = torch.nn.functional.one_hot(input, num_classes=5)
input = torch.tensor([[0, 1, 2, 3], [1, 2, 3, 4]])
output = torch.nn.functional