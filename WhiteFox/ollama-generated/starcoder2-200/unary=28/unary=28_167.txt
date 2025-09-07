

class Model(torch.nn.Module):
    def __init__(self, maxval=100):
        super().__init__()

        self.linear = torch.nn.Linear(784, 256)
 
    def forward(self, x1):
        v1  = self.linear(x1) 
        v2  = torch.clamp_min(v1, minval=0) 
        v3  = torch.clamp_max(v2, maxval=100)

        return v3


# Initializing the model
m  = Model()
