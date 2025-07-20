a = torch.IntTensor([1, 2, 3, 4, 5])
b = torch.IntTensor([6, 7, 8, 9, 10])
c = torch.IntStorage(a.size()[0])
for i in range(a.size()[0]):
    c[i] = (a[i] + b[i])