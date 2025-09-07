
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg1: int = 2395874060239875, arg2: int= 1):
        self.conv = torch.nn.Conv2d(arg1, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = torch.full([arg1, arg2], 1, dtype=torch.float32, layout="AS", device="cpu")
        v2  = convert_element_type(v1, dtype=torch.float64)
        v3  = torch.cumsum(v2, 1)

# Initializing the model