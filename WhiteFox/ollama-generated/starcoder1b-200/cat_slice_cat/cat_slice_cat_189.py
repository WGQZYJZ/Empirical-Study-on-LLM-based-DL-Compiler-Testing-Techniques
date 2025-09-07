
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        t1 = torch.cat([x1[:, 0:size], x1[:, size:]], dim=1)
        t2 = t1[:, 0:size] * 0.5
        t3 = t1[:, size:]  # Further slice the tensor along dimension 1
        t4 = torch.cat([t1, t3], dim=1)
        return t4


# Initializing the model
m = Model()

