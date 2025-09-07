
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1).view(x1.shape[0], -1) # View the output tensor to turn it into a vector (this will be the same as input x1)
        v2 = torch.cat([v1, v1, ..., v1], dim=1)  # Concatenate the two vectors from the last layer in the model to generate the output tensor
        return v2


# Initializing the model
m = Model()
x1 = torch.randn(2, 3, 64, 64)
