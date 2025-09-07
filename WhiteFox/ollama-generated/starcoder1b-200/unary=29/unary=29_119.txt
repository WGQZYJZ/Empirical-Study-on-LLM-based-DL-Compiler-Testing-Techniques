
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2dTranspose(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, min_value=None, max_value=None):
        v1 = self.conv(x1, min_value=min_value, max_value=max_value)
        return v1


# Initializing the model
m = Model()


