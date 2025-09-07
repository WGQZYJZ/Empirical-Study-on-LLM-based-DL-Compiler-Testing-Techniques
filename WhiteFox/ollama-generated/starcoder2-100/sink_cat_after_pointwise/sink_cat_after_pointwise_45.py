
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1, input2):

        v  = torch.cat([input1, input2], dim=0)
        return v[None]


# Initializing the model
m = Model()


# Inputs to the model