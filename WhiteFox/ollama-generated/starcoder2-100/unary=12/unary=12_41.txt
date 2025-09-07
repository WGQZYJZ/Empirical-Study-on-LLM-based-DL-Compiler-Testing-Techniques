
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x1):
        v1  = self.conv(x1)
        v4 = sigmoid(v1)
        v6  = v1 * v4
        return v6

m  = Model()

 # Inputs to the model
 x1  = torch.randn(20,3,65,70) 
 __output__  = m(x1)