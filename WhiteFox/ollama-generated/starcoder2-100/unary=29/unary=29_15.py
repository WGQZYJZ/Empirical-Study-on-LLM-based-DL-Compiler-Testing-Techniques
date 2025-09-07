
class Model(torch.nn.Module):
    def __init__(self, maxval=10):
        super().__init__()
        self.convt = torch.nn.ConvTranspose2d(3, 8, 4)
 
    def forward(self, x1):
        v1 = self.convt(x1)
        v2 = torch.clamp_min(v1, maxval=0) 
        v3 = torch.clamp_max(v2, minval=-99) # The minimum value is -99 and the maximum value depends on the `maxval` keyword argument passed when creating an instance of Model
        return v3


# Initializing the model with a different maximum value from that of the previous example.
m = Model(maxval=50)


# Inputs to the model, which will be used to generate a new model. This input will also be used to determine the new model output after generation
x1  = torch.randn(32, 8 ,64, 64) # The shape of this input is [32, 8, 64, 64]

