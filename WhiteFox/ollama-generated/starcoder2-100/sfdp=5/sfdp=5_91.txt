
class Attention(torch.nn.Module):
    def __init__(self, dmodel=768):
        super().__init__()
        self.query = torch.nn.Linear(dmodel, 256) 
        self.key   = torch.nn.Linear(dmodel, 256) 
        self.value = torch.nn.Linear(dmodel, dmodel)
        self.output_layer  = torch.nn.Linear(768 + 768, 1024)
 
    def forward(self, x):
        k  = self.key(x) 
        v  = self.value(x) 
        q  = self.query(k) 
        attn_mask = torch.zeros((q.size(-2), q.size(-3)), dtype=torch.bool).cuda() 
        for pos in range(0, k.size(-1)):
            attn_mask[pos] += -9e18
        attn_mask[:, :x.size(-1)]  = 1 # Make attention 1 on the diagonal
        v1  = torch.einsum('ijk->ik', q) + torch.einsum('ijl->il', k) 
        v2  = v1 / math.sqrt(q.size(-1)) 
        v3  = F.softmax(v2, dim=0) # Softmax along the batch dimension
        v4  = torch.dropout(v3, p=0.1, training=self._training) 
        v5  = torch.einsum('ijk->ik', k.transpose(-1,-2)) * v3 / math.sqrt(q.size(-1)) 
        v6  = torch.cat((x + v4.transpose(-1,-2), x @ (v5.transpose(-1, -2))), dim=-1)
        v7  = self.output_layer(v6).tanh() 
        return v7

# Initializing the model
model  = Attention()

 # Inputs to the model
x = torch.randn(4, 30, 768)

# Generate a new model, with different inputs x from previous model
new_m  = Model(x)

