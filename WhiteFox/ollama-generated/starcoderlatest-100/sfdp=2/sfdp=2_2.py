
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query_key = torch.nn.Linear(512, 384)
 
    def forward(self, x):
        v1 = self.query_key(x).transpose(-2, -1)
        v2 = v1.div(0.5)
        v3 = v1 * 1 / (torch.sqrt(v2))
        v4 = torch.nn.functional.softmax(v3, dim=-1)
        v5 = torch.nn.functional.dropout(v4, p=dropout_p)
        v6 = v5.matmul(value).transpose(-2, -1)
        return v6


# Initializing the model
m = Model()


# Inputs to the model
x  = torch.randn(1, 512, 7, 7)
