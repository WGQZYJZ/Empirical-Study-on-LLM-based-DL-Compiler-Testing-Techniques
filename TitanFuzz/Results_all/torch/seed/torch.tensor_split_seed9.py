data = torch.arange(16)
out = torch.tensor_split(data, 4, dim=0)
out = torch.tensor_split(data, 4, dim=0)
for i in out:
    print(i)
out = torch.tensor_split(data, [4, 6, 10], dim=0)
for i in out:
    print(i)