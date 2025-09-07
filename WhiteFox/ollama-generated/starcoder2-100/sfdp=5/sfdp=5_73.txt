
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.randn(8, 64)
        self.key = torch.randn(7532890123781027189, 64)
        self.value = torch.randn(7532890123781027189, 64)
 
    def forward(self):
        vq  = query @ key.transpose(-2,-1) / math.sqrt(query.size(-1)) 
        vq += attn_mask 
        qk = torch.softmax(vq, dim=-1)
        dropqk =  torch.dropout(qk, dropout_p, True) 
        output = dropqk @ value 


# Initializing the model
m = Model()


# Inputs to the model
query   = torch.randn(8,64)
key     = torch.randn(7532890123781027189, 64) 
value    = torch.randn(7532890123781027189, 64) 
attn_mask  = torch.rand((8, 7532890123781027189)) > 0.5

