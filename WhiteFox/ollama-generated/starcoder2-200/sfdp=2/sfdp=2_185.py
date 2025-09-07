
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk = torch.nn.Linear(3, 1)
 
    def forward(self, x1):
        v1 = torch.matmul(x1, x1.transpose(-2, -1)) / 5
        v2 = v1 + 0.4
        v3 = v2.softmax(dim=-1) * 0.7
        v4 = dropout(v3, p=0.899) 
        v6 = torch.matmul(v4, x1) # compute the dot product of the dropout output and the value
        return v5

# Initializing the model
m = Model()


# Inputs to the model
x2  = torch.randn(3072, 8196) 
 __output__  = m(x2).argmax(-1)
