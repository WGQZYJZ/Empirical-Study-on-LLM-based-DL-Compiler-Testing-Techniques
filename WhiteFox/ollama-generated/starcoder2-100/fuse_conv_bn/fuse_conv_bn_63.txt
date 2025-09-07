
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1):
        return self.convbn(input)

 # Inputs to the model
input = torch.randn(32, 64000000)
 
# Initializing the model
m = Model()
m.convbn = torch.nn.Conv2d(64000000, 512, 7).cuda().eval() # Conv2d is used as an example here to show the constraint. It doesn't matter which type of conv layer we choose.
