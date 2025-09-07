
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x):
        v = torch.cat((x[:, 0:2], x[:, 2:4]), dim=1)
        return torch.mean(v, 0)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 64, 64)
