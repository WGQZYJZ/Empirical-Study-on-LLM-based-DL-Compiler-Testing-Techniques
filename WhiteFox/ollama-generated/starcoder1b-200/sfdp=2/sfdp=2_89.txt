
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.nn.functional.dropout(v1, p=0.3)
        v2 = self.conv2(v2)
        return v2


# Initializing the model
m = Model()


