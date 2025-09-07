
class Attention(torch.nn.Module):
    def __init__(self, dim1=64, dim2=800):
        super().__init__()
        self.scale  = math.sqrt(dim1) # the square root of `dim` helps to stabilize the gradients 
        self.query  = torch.nn.Linear(in_features=dim2, out_features=dim1)
        self.key    = torch.nn.Linear(in_features=dim2, out_features=dim1)
        self.value  = torch.nn.Linear(in_features=dim2, out_features=dim1)
 
    def forward(self, query):
        v0 = self.query(query).softmax(dim=-1)
        v1 = self.key(query) * self.scale 
        v3 = self.value(v0).softmax()
        v4  = v2 @ v3 
        return v4


# Initializing the model
a  = Attention()

# Inputs to the model
query_tensor  = torch.randn(1, 64)
__output__    = a(query_tensor)