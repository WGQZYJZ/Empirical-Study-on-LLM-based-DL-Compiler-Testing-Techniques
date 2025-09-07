

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 * 0.5
        v3  = v1 ** 2
        v4  = v3 * v1 
        v5  = v4 * 0.044715
        v6  = v1 + v5 #t1
        v7  = v6* 0.7978845608028654 #t3
        v8  = torch.tanh(v7) #t8 
        v9  = v8 + 1 #t9
        v10 = v2 * v9#t2
        return v10


# Initializing the model
m_new = Model()


# Inputs to the model
x1_new = torch.randn(1, 3, 64, 64)

