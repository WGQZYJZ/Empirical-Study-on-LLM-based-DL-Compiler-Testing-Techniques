
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.other = torch.nn.Parameter(torch.randn([1]))
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + self.other 
        v3  = torch.relu(v2)
        return v3


# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn([8, 3, 64, 64]) 
 
# Setting other as a new tensor with same shape and type of the input x1
other  = m.conv(torch.rand([2] + list(m.conv.weight[0].shape)))
 
__output__  = m(x1)

