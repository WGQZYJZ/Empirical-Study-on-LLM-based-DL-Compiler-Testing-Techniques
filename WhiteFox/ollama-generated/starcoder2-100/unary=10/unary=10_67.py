
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(5, 1)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + 3 
        v3  = torch.clamp_min(v2, 0)
        v4  = torch.clamp_max(v3, 6)
        return v4 / 6


# Initializing the model and its input tensor x1:

m = Model()
x1  = torch.randn(5)

# Running the model:

__output__  = m(x1)