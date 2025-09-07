
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)
 
    def forward(self, x, other=None):
        v1 = self.linear(x)
        if other is not None:
            v2 = self.linear(other) + v1
        else:
            v2 = v1
        return relu(v2)


# Initializing the model
m  = Model()


