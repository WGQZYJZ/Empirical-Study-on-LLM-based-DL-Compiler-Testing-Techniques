tensor = torch.tensor([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
output = torch.nn.functional.one_hot(tensor, num_classes=(- 1))