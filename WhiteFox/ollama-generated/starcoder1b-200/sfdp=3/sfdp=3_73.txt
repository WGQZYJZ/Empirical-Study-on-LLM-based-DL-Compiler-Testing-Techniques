
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.dropout1 = torch.nn.Dropout(p=0.5)
        self.conv2 = torch.nn.Conv2d(8, 4, 1, stride=1, padding=1)
        self.dropout2 = torch.nn.Dropout(p=0.2)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v1 = self.dropout1(v1)
        v2 = self.conv2(v1)
        v2 = self.dropout2(v2)
        return v2


# Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
