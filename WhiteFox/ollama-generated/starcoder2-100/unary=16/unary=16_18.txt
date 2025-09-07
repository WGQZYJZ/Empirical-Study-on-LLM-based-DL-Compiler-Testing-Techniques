
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(16 * 4* 3, 20)

    def forward(self, x1):
        v1 = linear(x1)
        v2 = relu(v1)
        return v2


# Initializing the model
m  = Model()


# Inputs to the model