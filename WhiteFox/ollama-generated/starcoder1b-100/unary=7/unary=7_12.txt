
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8, bias=False)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        clamped_output = (0 < v1).float() * v1 + (v1 - 0) * (3 / 6)
        return clamped_output


# Initializing the model
m = Model()


