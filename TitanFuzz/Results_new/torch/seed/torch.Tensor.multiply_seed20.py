a = torch.tensor(3.0)
b = torch.tensor(4.0)
c = torch.tensor(5.0)
d = torch.tensor(6.0)
e = (a * b)
f = (c * d)
values = [a, b, c, d]
for i in range(len(values)):
    for j in range(len(values)):
        print(torch.Tensor.multiply(values[i], values[j]))