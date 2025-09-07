
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.key = torch.nn.Linear(1024, 64)
        self.query = torch.nn.Linear(1024, 32)
 
    def forward(self, x1):
        v1  = self.query(x1)
        v2  = self.key(v1).transpose(-2, -1)
        v3  = v2 * scale_factor
        v4  = v3.softmax(dim=-1) 
        v5  = torch.nn.functional.dropout(v4, p=dropout_p)
        v6  = v5.matmul(value)

        return v6


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(20, 3, 8, 10).to('cuda:0')
__output__  = m(x1)