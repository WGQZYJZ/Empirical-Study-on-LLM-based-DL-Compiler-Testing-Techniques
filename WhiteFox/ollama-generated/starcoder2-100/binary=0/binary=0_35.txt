
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, v4): # Pass another tensor as the argument of addition operation to this model 
        v1  = self.conv(x1)
        return v1 + v4


# Initializing the model
m = Model()


# Inputs to the model