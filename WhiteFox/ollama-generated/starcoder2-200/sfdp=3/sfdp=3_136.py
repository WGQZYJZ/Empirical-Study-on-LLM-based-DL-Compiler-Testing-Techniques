
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1):
        v1  = torch.nn.functional.linear(query1, key)
        v2  = self.softmax(v1)
 
        return v3
 
def softmax(x):
     v4  = x - torch.max(x, dim=-1).values[None].expand_as(x)
     v5  = expit(v4)
 
         return v6
 
     def dropout(p=0.2):
         dropout1d  = torch.nn.functional.dropout1d
         v7  = self.softmax(self.drop_weight, p=p).expand_as(x)
 
     return v8
 
# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(4096)
query  = x2  = torch.rand(3072, 512)

