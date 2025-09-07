
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other 
        return torch.relu(v2)


# Initializing the model
m = Model()
 
# Inputs to the model
other = torch.randn(8, 64, 64) # Any tensor with shape (8 x 64 x 64), this is an additional input for the model that has not been used before in this model’s definition

