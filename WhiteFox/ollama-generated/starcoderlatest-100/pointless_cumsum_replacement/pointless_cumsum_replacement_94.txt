
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = torch.full([x1.shape[0], x1.shape[2]], 1, dtype=torch.float64) 
        v2 = convert_element_type(v1, x2.dtype) 
        v3 = torch.cumsum(v2, 1)
        return v3


# Initializing the model
m = Model()

