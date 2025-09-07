
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query):
        key = torch.randn(*query.size())  # Generate a random tensor with the same size as the input
        attn_mask  = 1 - torch.eye(len(query), device=query.device) 
        v1  =  query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        v2  =   v1 + attn_mask
        v3  =  torch.softmax(v2, dim=-1)
        return  (v3@ value)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4096,)
__output__  = m(x1)

