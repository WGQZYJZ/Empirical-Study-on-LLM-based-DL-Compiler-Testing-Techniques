data1 = torch.randn(5, 2)
targets1 = torch.empty(5, dtype=torch.long).random_(2)
data2 = torch.randn(3, 2)
targets2 = torch.empty(3, dtype=torch.long).random_(2)
dataset = torch.utils.data.ConcatDataset([data1, data2])
for i in dataset:
    print(i)