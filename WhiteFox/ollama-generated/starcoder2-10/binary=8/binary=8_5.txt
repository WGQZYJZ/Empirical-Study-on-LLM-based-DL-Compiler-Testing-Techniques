
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + other 
        return v2
 
# Initializing the model with "other" parameter to be passed in as a keyword argument during execution of the model
m = Model()


# Inputs to the model including another tensor as a keyword argument for addition operation
x1 = torch.randn(1, 3, 64, 64) # Input for conv function call
other = torch.randn(2, 5, 8, 7)# A different tensor that is passed in as a keyword argument for the conv operation


# Model execution
__output__  = m(x1).mean()