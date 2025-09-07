
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk = torch.nn.Linear(8, 4)
 
    def forward(self, q1, k1):
        v2 = self.qk(q1) * scale_factor
        v3 = v2.softmax(-1)
        v6 = torch.nn.functional.dropout(v3, p=0.75).matmul(k1)
        return v6


# Initializing the model
m  = Model()


# Inputs to the model
q1 = torch.randn(2, 8) + 0.5
k1 = torch.randn(4, 8) - 0.75

__output__  = m(q1, k1)
