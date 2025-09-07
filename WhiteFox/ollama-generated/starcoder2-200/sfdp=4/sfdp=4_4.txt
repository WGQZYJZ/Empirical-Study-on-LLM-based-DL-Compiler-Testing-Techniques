
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        attn = torch.softmax(query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)), dim=-1) + 0.3
        return (attn @ value)
 

# Initializing the model
m  = Model()

 # Inputs to the model
query_1 = torch.randn(3, 56*8*2+7, 14*29*8*16*15*16*29*8*8, requires_grad=True)
key    = query_1.transpose(-2,-1) + query_1 + query_1 -query_1
value   = torch.randn(3, 14*29*7*7*7*7*7*56*56 , requires_grad=True) * (0.8 if query_1 else 0.5 if key else 0.7071067811865476)
attn = torch.nn.Dropout(p=0.2)(torch.randn(*value.shape))
attn += torch.tensor(2.3).view([*value.shape[:-1],1])
__output__  = m(query_1, key, value)

