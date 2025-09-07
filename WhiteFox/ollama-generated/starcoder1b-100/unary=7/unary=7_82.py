
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        clamped_output = clamp(min=0, max=6, l1 + 3)
        v2 = v1 * clamped_output
        return v2


# Initializing the model
m = Model()

