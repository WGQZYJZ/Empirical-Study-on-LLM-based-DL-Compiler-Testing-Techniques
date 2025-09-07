
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale  = torch.nn.Parameter(torch.tensor(0))
        self.dropout  = torch.nn.Dropout(p=1)
 
    def forward(self, qry, key, value):
        v1  = torch.matmul(qry, key.transpose(-2, -1)) # Compute the dot product of a query and a key tensor
        v2  = self.scale * v1
        v3  = v2.softmax(dim=-1)
        v4  = dropout_qk = self.dropout(v3)
        return v4


# Initializing the model
m = Model()

# Inputs to the model
qry, key, value = torch.randn(20), torch.randn(20), torch.randn(512, 10)
__output__  = m(qry, key, value)

