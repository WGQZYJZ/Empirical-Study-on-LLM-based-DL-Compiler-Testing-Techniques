
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul = torch.nn.Linear(2, 3)
 
    def forward(self, q, k, v):
        v1 = self.matmul(q).transpose(-1, -2)
        v2 = torch.matmul(v1, k.transpose(-1, -2))
        v3 = v2 / math.sqrt(v2.shape[-1])
        v4 = torch.nn.functional.dropout(v3, p=dropout_p).softmax(dim=-1) * v2
        output  = torch.matmul(v4, v)
        return output


# Initializing the model
m = Model()

# Inputs to the model
q = torch.randn(1, 2, 3)
k = torch.randn(1, 2, 3)
v = torch.randn(1, 2, 4)
