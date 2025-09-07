
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256, 3)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.sigmoid(v1)
        return v2

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(32, 56*56) # The input size is randomly generated using 56 x 56 as the output size of a convolutional layer that has 56 outputs and 48 outputs as the number of input channels
