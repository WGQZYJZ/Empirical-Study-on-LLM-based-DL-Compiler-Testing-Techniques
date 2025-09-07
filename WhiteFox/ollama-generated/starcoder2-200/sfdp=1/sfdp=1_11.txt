
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1 = torch.matmul(query, key.transpose(-2,-1))
        v2 = v1 / 0.5 
        v3 = v2.softmax(dim=-1)
        return v3


# Initializing the model
m = Model()
 
