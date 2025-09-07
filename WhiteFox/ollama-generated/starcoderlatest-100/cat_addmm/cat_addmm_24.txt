
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 16, 5)
        # Initialize the weights of the first fully connected layer to be random numbers between -0.1 and 0.1.
        self.fc_layer_weights = nn.Parameter(torch.randn(-0.1, 0.1, (256, 500)))
 
    def forward(self, x1):
        v1 = torch.addmm(x1, self.fc_layer_weights, x1)
        v2 = torch.cat([v1], dim=1)
        return v2


# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
