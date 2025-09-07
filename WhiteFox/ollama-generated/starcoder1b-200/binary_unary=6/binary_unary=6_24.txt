
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 10)

    def forward(self, x):
        v1 = self.linear(x)
        other  = 0.25*torch.randn_like(v1)
        v2 = v1 - other
        return relu(v2)


# Initializing the model
m = Model()

