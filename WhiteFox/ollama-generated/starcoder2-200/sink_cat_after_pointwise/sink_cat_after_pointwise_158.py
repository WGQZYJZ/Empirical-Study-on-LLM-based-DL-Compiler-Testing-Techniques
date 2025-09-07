
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t  = torch.cat([x1[0], x1[3]], dim=2)
        t  = t.view(-1, 4)
        return torch.relu(t)


# Initializing the model
m  = Model()

 # Inputs to the model
x1 = [torch.randn(5), torch.randn(7)]
