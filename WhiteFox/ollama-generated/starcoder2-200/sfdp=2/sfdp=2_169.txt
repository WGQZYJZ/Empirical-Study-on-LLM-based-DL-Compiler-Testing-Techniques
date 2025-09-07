
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.matmul(x1, torch.randn(32, 64)) 
        v2  = v1 / math.sqrt(5)
        v3  = v2.softmax(-1)
        v4  = torch.nn.functional.dropout(v3, p=0.789)
        v5  = v4 @ torch.randn(64, 64) 
        return v5


# Initializing the model
m = Model()
__output__  = m(torch.randn(2, 32))