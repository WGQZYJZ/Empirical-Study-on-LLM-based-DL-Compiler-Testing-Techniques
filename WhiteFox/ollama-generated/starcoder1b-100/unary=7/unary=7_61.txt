
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 8, bias=True)

    def forward(self, x1):
        v1 = self.linear(x1) * clamped_output
        return v2


# Initializing the model
m = Model()


