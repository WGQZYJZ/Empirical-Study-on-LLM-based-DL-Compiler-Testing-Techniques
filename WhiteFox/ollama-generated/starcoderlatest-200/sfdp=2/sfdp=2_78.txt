
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout1 = torch.nn.Dropout2d(p=0)
        self.conv = torch.nn.Conv2d(8, 4, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = torch.cat((x1, x1), dim=1) # Concatenate the two inputs along channel dimension to produce a feature map with two channels
        v2 = self.dropout1(v1)
        v3 = self.conv(v2)
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 8, 64, 64)
