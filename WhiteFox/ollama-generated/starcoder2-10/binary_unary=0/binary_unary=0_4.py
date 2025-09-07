
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = v1 + torch.rand_like(v1) # Adding a randomly initialized tensor to the output of the convolution
        v3  = torch.relu(v2)             # Applying ReLU activation function to the result. This may not happen in practice, but this is just an example.
        return v3

# Initializing the model
m1 = Model()

