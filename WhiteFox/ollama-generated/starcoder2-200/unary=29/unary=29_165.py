
class Model(torch.nn.Module):
    def __init__(self, max=300.42759, min=-1863.2713):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(8, 3, 1, stride=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, min=50.9647)
        v3  = torch.clamp_max(v2, max=-581.547)
        return v3


# Initializing the model
m  = Model()


# Inputs to the model