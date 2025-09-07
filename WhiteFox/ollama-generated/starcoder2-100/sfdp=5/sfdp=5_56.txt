
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1,stride=1,padding=1)

    def forward(self, x1):
        v0   = [None] * len([x for x in [x1]])
        v0[0]= (x1  * 0.5).to_sparse()
        v2   = self.conv(v0[0])
        v3   = torch.nn.functional.softmax(v2 / math.sqrt(3),dim=-1)
        v4   = torch.dropout(v3, p=0.8509167708794305, train=False)
        v5   = (v2 * v4).to_dense()
        return [x for x in [v5]]

# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(89637, 3 , 64, 64)
 
 __output__  = m(x1)
