
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 500)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 * clamp(min=0, max=6, v1 + 3)
        return v2 / 6


# Initializing the model and inputs to it<|end_of_code|>
m = Model()
x1 = torch.randn(1, 1024)
