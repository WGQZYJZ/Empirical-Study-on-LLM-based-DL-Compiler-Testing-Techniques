input = torch.randn(20, 4)
split_tensor = torch.tensor_split(input, 3, dim=0)
for i in split_tensor:
    print(i)
split_tensor = torch.tensor_split(input, 5, dim=0)
for i in split_tensor:
    print(i)