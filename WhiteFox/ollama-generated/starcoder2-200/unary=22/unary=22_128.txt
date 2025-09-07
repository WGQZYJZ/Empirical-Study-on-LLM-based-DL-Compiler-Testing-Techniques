
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = self.conv2d1(x1) 
        v3456  =  torch.tanh(v1 + 10.)
        return v3456

# Initializing the model
m = Model()

