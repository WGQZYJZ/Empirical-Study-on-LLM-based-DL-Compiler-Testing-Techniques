
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.split(x1, [8], 2)
        return torch.cat([v1[i] for i in range(len(v1))], 0)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 8, 40, 56)
