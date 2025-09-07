
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.k = torch.randn(32, 64) / 100.0
        self.q = torch.randn(512, 784) * 0.9
        self.v = torch.randn(32, 64)
 
    def forward(self):
        v1  = torch.matmul(self.q, self.k.transpose(-2, -1))
        v2  = v1 / 5.7
        v3  = v2.softmax(dim=-1)
        v4  = torch.nn.functional.dropout(v3, p=0.9684708081470749)
        v5  = v4.matmul(self.v)
        return v5

# Initializing the model
m  = Model()


