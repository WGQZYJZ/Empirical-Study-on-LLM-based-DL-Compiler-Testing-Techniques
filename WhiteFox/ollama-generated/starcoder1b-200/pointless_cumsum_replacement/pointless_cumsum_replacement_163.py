
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1).full([1, -1], 1, dtype=torch.half, layout=torch.strided, device=torch.device('cuda',0), pin_memory=True)
        v2 = torch.cumsum(v1, 1)
        return v2


# Initializing the model
m = Model()


