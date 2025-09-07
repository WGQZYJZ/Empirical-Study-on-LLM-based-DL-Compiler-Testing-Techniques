
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1):
        qk  = torch.bmm(input1, key) / math.sqrt(query.size(-1))
        qk  = qk + attn_mask
        attn_weight  = torch.softmax(qk, dim=-1) 
        output   = attn_weight @ value

        return output

# Initializing the model
m = Model()

# Inputs to the model
key  = torch.randn(32, 64, 64) # A tensor of size [batchsize, inputdim]
query  = torch.randn(32, 128, 64) # A tensor of size [batchsize, keydim, querydim] 
attn_mask   = torch.ones([32, 64, 1])

