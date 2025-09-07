
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.cat([x2 for _, x2  in inputs])
        v2 = v1.view(-1)
        v3 = torch.relu(v2)

m = Model()
for i in range(len(inputs)):
    __output__[i]  = m({k:inputs[i][0], k:inputs[i][1]})

