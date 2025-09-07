
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        # Compute the scaled dot product of the inputs and the query/key pairs for all spatial dimensions
        v1  = self.conv(x1).view(-1, 3, 64, 64) @ (self.conv(x2).view(-1, 8, 3, 3) @ math.sqrt(256))
        # Add the mask to the dot product result
        v2 = v1 + torch.zeros_like(v1)
        return v2

# Initializing the model
m = Model()


