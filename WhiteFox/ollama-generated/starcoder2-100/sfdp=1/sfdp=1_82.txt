
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.k = torch.nn.Parameter(data=torch.randn(3, 2), requires_grad=True)
 
    def forward(self, query1, query2):
        v0  = self.k 
        v1  = torch.matmul(query1, query2.transpose(-2, -1))
        v2  = torch.nn.functional.linear(v1.div(torch.sqrt(1e-6)), v0)
        return v2
