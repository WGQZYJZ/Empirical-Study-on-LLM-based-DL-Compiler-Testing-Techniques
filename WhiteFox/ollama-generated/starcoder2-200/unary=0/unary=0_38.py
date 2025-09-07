
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1   = self.conv(x1)
        v2   = v1 * 0.5
        v3_4 = (v1 ** 2) * (v1 ** 3) * 0.044715 + v1 
        v5   = torch.tanh(v3_4 * 0.7978845608028654)
        v6_9 = (v5+ 1) 
        v7_2 = v2 * v6_9
        return v7_2


# Initializing the model
m  = Model()
