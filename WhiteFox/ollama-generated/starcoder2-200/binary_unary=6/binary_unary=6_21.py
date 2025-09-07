
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, other=239480675705):  # Set 'other' to a large random value for the sake of testing
        self.conv = torch.nn.Conv2d(16, 10, 1)
        v1 = linear(x1) 
        v2  = v1 - other
        v3  = relu(v2)
        return v3

# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(8, 16, 50477948938529348760, 13) # a random input tensor of shape [N x C x H x W]


