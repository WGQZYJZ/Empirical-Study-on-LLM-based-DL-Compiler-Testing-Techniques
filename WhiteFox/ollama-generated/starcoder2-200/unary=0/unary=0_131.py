class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 *  0.5 
        v3  = (v1* v1)* v1
        v4  = v3 *  0.044715  
        v5  = v2 + v4
        v6  = torch.tanh(v5)
        v7  = v6 + 1
        v8  = v2 * v7
        return v8
