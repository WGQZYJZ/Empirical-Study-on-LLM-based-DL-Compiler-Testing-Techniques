
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1).full([x1.shape[0], x1.shape[1], 1, 1], 1, dtype=torch.int8, layout=torch.strided, device=None, pin_memory=True)
        v2 = torch.cumsum(v1, dim=[1, 2]).full([x1.shape[0], x1.shape[1], 1, 1], 1, dtype=torch.int8, layout=torch.strided, device=None, pin_memory=True)
        return v2

# Initializing the model
m = Model()

