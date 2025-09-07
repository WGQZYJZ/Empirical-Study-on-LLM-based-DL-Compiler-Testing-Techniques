
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = x1.permute(...)
        return torch.functional.linear(...)

 # Initializing the model
m = Model()
 # Inputs to the model
x1 = torch.randn(1, 2, 3)
