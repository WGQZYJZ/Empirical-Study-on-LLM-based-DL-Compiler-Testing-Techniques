
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1).sum(dim=-2, keepdim=True)  # Calculate the sum of all channels in the first convolutional layer and add them to input tensor
        v2 = torch.cat([v1, x2], dim=-2)        # Calculate sum of two channels and concat it to a third dimension
        return v2


# Initializing the model
m = Model()


