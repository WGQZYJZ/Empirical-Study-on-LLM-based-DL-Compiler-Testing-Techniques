
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1,stride=1,padding=1)
        self.linear = nn.Linear(50*7*7,4)
 
    def forward(self, x1):
        v1  = conv(x1)
        v2  = v1 * 0.5
        v3  = v1 * 0.7071067811865476
        v4  = torch.erf(v3)
        v5  = v4 + 1 
        v6  = v2 * v5
        linear_layer = nn.Linear(6*6,4).cuda()
        y1 = linear_layer(v6.view(-1))
 
        return y1

# Initializing the model
m = Model()

