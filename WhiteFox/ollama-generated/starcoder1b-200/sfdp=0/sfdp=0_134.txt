
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.fc   = torch.nn.Linear(4 * 4, 8)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = v1  * 0.5
        v3 = v1  * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4  + 1
        v6 = (v2 * v5).softmax(-1)
        v7 = self.fc(torch.cat((x2, v6), dim=-1))
        return v7


# Initializing the model
m  = Model()

