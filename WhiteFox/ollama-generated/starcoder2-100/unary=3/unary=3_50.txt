
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2  = self.conv(x1)
        v3  = torch.sigmoid(v2*0.5) # Apply the sigmoid function to the output of the convolution and multiply by constant 0.5. 
        return v4
 
# Initializing the model
m = Model()


