
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1234, key0123456789):
        v1  = torch.einsum("b i d, b j d -> b i j", query1234, key0123456789) 
        v2  = v1 / math.sqrt(query1234[...,:,-1])
        v3  = v2 + attn_mask
        attn_weight  = torch.softmax(v3, dim=-1)
        attn_weight  = torch.dropout(attn_weight, dropout_p, True) 
        return attn_weight  @ value


# Initializing the model
m = Model()

# Inputs to the model
query1234  =  torch.randn(batchsize1, length1, dim2, 697058, requires_grad=True)
key0123456789   =  torch.randn(batchsize2, length1 + 697058 - 5 , dim2, 697058, requires_grad=True)

 # Initializing the model, and running it on inputs of valid sizes
m(query1234, key0123456789)