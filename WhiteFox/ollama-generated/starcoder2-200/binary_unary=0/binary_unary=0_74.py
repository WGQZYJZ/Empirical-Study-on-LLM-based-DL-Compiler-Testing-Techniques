
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.other = torch.zeros([4] * 5).to(torch.float64)
 
    def forward(self, x):
        v1  = self.conv(x) + self.other
        v2  = torch.relu(v1)
        return v2


# Initializing the model
m = Model()
__output__  = m(torch.randn([8] * 5))
