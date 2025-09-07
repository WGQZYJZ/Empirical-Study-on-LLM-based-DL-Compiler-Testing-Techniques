
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk  = torch.nn.Linear(256, 4096)
 
    def forward(self, query):
        key  = torch.randn(1, 384, 7, 7)
        value  = torch.randn(1, 4096, 14, 14)
 
        v1 = self.qk(query).div(256 * math.sqrt(self.__dropout_p))
        v2  = query 
        v3 = key.transpose(-2, -1) / torch.pow(256, 0.5) * __dropout_p
        v4 = torch.nn.functional.softmax(v3, dim=-1)
        v5  = value
        v6  = dropout_qk.matmul(value)
        return v6


# Initializing the model
m = Model()
 
# Inputs to the model
query  = torch.randn(4096, 7, 7)
__output__  = m(x1)

