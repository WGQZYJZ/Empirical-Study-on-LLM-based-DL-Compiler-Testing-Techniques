
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(512, 30768)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 * clamp(min=0, max=6, l1 + 3) # The following line is added here!
        v3 = v2 / 6 # The following line is added here!
        return v3


# Initializing the model and generating inputs to it
m  = Model()
 
x1 = torch.randn(4096, 512)
__output__  = m(x1)


