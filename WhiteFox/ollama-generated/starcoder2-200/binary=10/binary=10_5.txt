
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(512, 512)
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1)
        if other is None:
            raise ValueError("other must be specified")
        return v1 + other


# Initializing the model
m = Model()
 
# Inputs to the model 
x1 = torch.randn(3,512)

