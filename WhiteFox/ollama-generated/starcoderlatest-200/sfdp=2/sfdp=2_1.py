
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_q = torch.nn.Linear(3, 64, bias=False)
        self.linear_k = torch.nn.Linear(3, 64, bias=False)
        self.linear_v = torch.nn.Linear(3, 128, bias=False)
 
    def forward(self, q, k, v):
        # Apply linear transformation to the query, key, and value tensor
        xq = self.linear_q(q)
        xk = self.linear_k(k)
       xv = self.linear_v(v)
        return xq, xk, xv


# Inputs to the model
q = torch.randn(1, 3, 64, 64)
k = torch.randn(256, 3, 64, 64)
v = torch.randn(1024, 3, 64, 64)
