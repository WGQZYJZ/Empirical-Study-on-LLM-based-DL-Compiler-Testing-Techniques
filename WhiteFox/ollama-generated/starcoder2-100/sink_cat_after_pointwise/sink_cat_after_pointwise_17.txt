
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1, input2):
       v = torch.cat([input1, input2], 0)
       return torch.relu(v).view(-1, 4*5)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 10, 1) + 2
x2 = torch.zeros((7, 1))
