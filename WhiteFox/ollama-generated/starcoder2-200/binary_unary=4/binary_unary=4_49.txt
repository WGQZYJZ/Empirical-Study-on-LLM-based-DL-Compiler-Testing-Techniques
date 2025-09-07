
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.linear = torch.nn.Linear(4096, 512)

    def forward(self, x1):
       v1  = self.linear(x1)
       v2  = v1 + other 
       return relu(v2)

# Initializing the model with a custom tensor passed to the argument `other` in the constructor.
m  = Model(torch.randn(4096,512))

