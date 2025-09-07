
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(512, 8)

    def forward(self, query=None, key=None, value=None):
        if value is not None:
            v1 = torch.softmax(query @ key.transpose(-2, -1), dim=-1)
        else:
            v0 = self.attn(query, key)[0]

        return v0


# Initializing the model
m  = Model()
 
# Input to the model, as an example where value is not None
q  = torch.randn(8, 4, 512)
k  = torch.randn(8, 3, 512)
v0  = m(query=q, key=k, value=None)
 
# Input to the model as an example where value is not None, and query is an additional input
q  = torch.randn(7, 4, 512) # Notice that q has one extra dimension compared to k in the example above
k  = torch.randn(8, 3, 512)
v0  = m(query=q, key=k, value=None)
 
# Input to the model as an example where query is not None, key and value are None
q  = torch.randn(7, 4, 512) # Notice that q has one extra dimension compared to k in the example above
v0  = m(query=q, key=None, value=None)

