
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.mm(x1[0], x1[2])
        return [v1] * len(x1)


# Initializing the model
m = Model()


# Inputs to the model (list containing three tensors of the same shape)
x1 = []
for i in range(3):
    t  = torch.randn([64, 50])
    x1.append(t)


__output__  = m(*x1)



