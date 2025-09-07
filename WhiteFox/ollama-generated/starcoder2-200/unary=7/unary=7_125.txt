
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 32)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 * clamp(min=0, max=6, l1 + 3) / 6
        return v2


# Initializing the model and inputs to the model. 
model = Model()
input_tensor = torch.randn((5, 10))

