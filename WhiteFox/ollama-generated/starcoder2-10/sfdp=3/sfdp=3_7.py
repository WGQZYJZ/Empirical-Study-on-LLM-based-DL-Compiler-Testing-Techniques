
class MyModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, v1037):
        self.conv = torch.nn.Conv2d(64, 8, 5)
        self.act = torch.nn.ReLU()

        v1095  = self.conv(v1037)
        v1096  = v1095 * 0.5
        v1097  = v1095 * 0.7071067811865476

        v1098  = torch.erf(v1097)
        v1099  = v1098 + 1
 
        v1038  = self.act(v1096 * v1099)
        v1102  = self.act(v1038)

        return (self.conv(v1102))
