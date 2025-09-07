
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(768, 768)
        self.ln1 = torch.nn.LayerNorm()
 
    def forward(self, xq, k, v):
        qk = attn(xq + k.transpose(-2,-1)) / math.sqrt(k.size(-1)) 
        qk += self.attn_mask  # mask the query-key dot product
        attn_weight = torch.softmax(qk, dim=-1)
        return attn_weight @ v
 

# Initializing the model
m  = Model()


# Inputs to the model
xq = torch.randn(64,768).unsqueeze(2).repeat(1,1,32,1) # query vector
k = torch.randn(512,768) # key matrix with 512 keys in each row of the matrix and 768 dimensions per key
v = torch.randn(32,512,768)


