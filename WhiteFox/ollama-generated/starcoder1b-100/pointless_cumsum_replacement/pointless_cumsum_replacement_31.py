
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1).type(torch.float64)
        v2 = convert_element_type(v1, torch.int64)
        v3 = torch.cumsum(v2, 1).type(torch.uint8)
        return v3


# Initializing the model
m = Model()


