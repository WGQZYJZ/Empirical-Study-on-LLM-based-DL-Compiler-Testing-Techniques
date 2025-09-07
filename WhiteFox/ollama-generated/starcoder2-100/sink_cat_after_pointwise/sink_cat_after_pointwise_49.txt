
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.cat([x1[0], x1[3]], dim=1)
        return torch.relu(v1).view(-1, 256),


# Initializing the model
m = Model()


# Inputs to the model
x1  = [torch.randn(48)] * 7

 