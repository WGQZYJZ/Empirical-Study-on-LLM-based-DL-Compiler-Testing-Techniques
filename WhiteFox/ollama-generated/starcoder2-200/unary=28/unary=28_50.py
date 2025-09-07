
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 4)

    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 - min_value if v1 > max_value else \
            v1 + (max_value - v1).relu()
        return v2


# Initializing the model
m  = Model()

# Inputs to the model