
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1,stride=1,padding=0)
        self.other  = torch.randn([4])
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 - self.other # subtract other from output of conv
        v3  = F.relu(v2)
        return v3


m  = Model()

# Initializing the model
x1  = torch.randn([5, 3, 64, 64])
__output__  = m(x1)

