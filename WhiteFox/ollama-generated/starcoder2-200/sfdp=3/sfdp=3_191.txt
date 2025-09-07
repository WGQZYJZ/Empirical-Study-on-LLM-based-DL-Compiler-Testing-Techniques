
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul  = torch.nn.functional.linear
        self.dropout = torch.nn.functional.dropout
 
    def forward(self, query, key, value, scale_factor=1., dropout_p=.0): 
        v1  = torch.nn.functional.softmax(torch.matmul(query, key.transpose(-2, -1).mul_(scale_factor)))
        v2  = self.dropout(v1)
        __output__  = v2 @ value

        return __output__


# Initializing the model
m = Model()

# Inputs to the model
key   = torch.randn(3, 64, 10)
value = torch.randn(3, 589824, 768)
scale_factor  = .0001 # random
dropout_p     = .0
query         = torch.randn(3, 2340, 768)
__output__    = m(query, key, value)

