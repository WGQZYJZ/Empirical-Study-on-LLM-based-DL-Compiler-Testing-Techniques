
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Parameter(torch.randn(3, 4))
        self.key   = torch.nn.Parameter(torch.randn(20, 7, 15))
        self.value = torch.nn.Parameter(torch.randn(8, 9, 15))
 
    def forward(self):
        v1  = torch.matmul(self.query, self.key.transpose(-2, -1))
        v2  = v1 / 0.7071067811865476
        v3  = torch.nn.functional.softmax(v2, dim=-1)
        v4  = torch.nn.functional.dropout(v3, p=0.5)
        __output__  = self.value * v4
        return __output__.sum()

# Initializing the model
m  = Model()

