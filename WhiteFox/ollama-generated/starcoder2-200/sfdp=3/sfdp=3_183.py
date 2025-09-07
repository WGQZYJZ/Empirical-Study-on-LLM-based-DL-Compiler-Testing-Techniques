
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale  = 1
        self.drop  = torch.nn.Dropout(0)
        self.key  = torch.randn(3, 4, 5)
 
    def forward(self, query):
        v1  = torch.matmul(query, key.transpose(-2, -1)) 
        v2  = v1 * self.scale
        v3  = v2 .softmax(dim=-1)
        v4  = self.drop(v3)
        return v4.matmul(value)

# Initializing the model with 0 as the initial scale factor and no dropout applied to the softmax output. 
m  = Model()

# Inputs to the model (query, key, value), where the query tensor is of shape [3 x 5]
query = torch.randn(3, 5)
key = m.key
value = torch.randn(3, 4, 5)
__output__  = m(query)

