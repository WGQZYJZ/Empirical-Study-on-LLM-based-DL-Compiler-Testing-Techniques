
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(3, 1)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.clamp_min(v1, min_value=-4096.) # Replace -4096. by an appropriate value.
        v3  = torch.clamp_max(v2, max_value=4095.) # Replace 4095. by an appropriate value.
        return v3


# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(1, 3)

__output__  = m(x1).sum()

