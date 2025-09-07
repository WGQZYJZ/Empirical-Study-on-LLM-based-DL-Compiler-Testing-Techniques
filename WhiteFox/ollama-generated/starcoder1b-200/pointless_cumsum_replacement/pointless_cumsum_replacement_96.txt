
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        t1 = torch.full([4], 1, dtype=torch.float64, layout='cpu', device='cuda')
        t2 = convert_element_type(t1, torch.float64)
        t3 = torch.cumsum(t2, 1)
        v3 = t3 * 2
        return v3

 # Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
