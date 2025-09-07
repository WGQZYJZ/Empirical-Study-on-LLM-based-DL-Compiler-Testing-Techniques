
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        t1 = torch.full([10, 10], 1, dtype=torch.float64, device='cpu')
        t2 = convert_element_type(t1, torch.double)
        t3 = torch.cumsum(t2, 1)
        return t3


# Initializing the model
m = Model()

