
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1).view((1, -1)) * 0.5
        v2 = v1  *  v1  *  v1
        v3 = v2  * 0.044715
        v4 = (v3  *  v1  * 0.7978845608028654).view((1, -1)) + 1
        v5 = v2  *  v4
        v6 = v5  * 0.7978845608028654
        v7 = torch.tanh(v6) + 1
        v8 = v5  *  v7
        return v8


# Initializing the model
m = Model()


