
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q1, k1, v1):
        r  = torch.matmul(q1, k1.transpose(-2, -1)) / (inv_scale_factor) 
        s  = r.softmax(dim=-1)
        o1  = torch.nn.functional.dropout(s, p=dropout_p) * v1
        return o1


# Initializing the model
m = Model()

# Inputs to the model
q1 = torch.randn(4, 32, 64)
k1 = torch.randn(50, 32, 64)
v1 = torch.randn(4, 50, 97)

__output__  = m(q1, k1, v1)

