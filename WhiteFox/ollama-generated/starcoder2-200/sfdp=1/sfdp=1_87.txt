
class Model(torch.nn.Module):
    def __init__(self, num_heads=8, embedding_dim=32):
        super().__init__()
        self.query  = torch.nn.Linear(embedding_dim, num_heads) 
        self.key = torch.nn.Linear(embedding_dim, num_heads)
        self.value = torch.nn.Linear(embedding_dim, num_heads)
 
    def forward(self, x1):
        
        v1  = self.query(x1).div(5.)
        v2  = self.key(v1).transpose(-2, -1)
        v3  = v1.softmax(dim=-1)
        v4  = torch.nn.functional.dropout(v3, p=0.6795783132530128)
        __output__  = self.value(v4).div_(math.sqrt(inv_scale_factor))
        
        return __output__

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(6, 3072)


