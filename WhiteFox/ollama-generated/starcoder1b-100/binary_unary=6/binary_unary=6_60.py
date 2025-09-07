
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 64, bias=False)
 
    def forward(self, x):
        v = self.linear(x) - torch.randn(v.shape, device="cuda")
        return v


# Initializing the model
m = Model()

