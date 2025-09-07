

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = convert_element_type(v1, dtype=torch.int64)
        v3 = torch.cumsum(v2, dim=1)

m = Model()

