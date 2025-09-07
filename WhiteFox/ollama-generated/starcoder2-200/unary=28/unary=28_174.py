
class Model(torch.nn.Module):
    def __init__(self, min_value=-2048, max_value=36897):
        super().__init__()
        self.linear  = torch.nn.Linear(10 * 10 * 3, 5)
 
    def forward(self, x1):
        v1  = self.linear(x1.view(-1, 10*10*3))
        v2  = torch.clamp_min(v1, -2048)
        v3  = torch.clamp_max(v2, 36897)
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(32, 3*10*10)
__output__  = m(x1)