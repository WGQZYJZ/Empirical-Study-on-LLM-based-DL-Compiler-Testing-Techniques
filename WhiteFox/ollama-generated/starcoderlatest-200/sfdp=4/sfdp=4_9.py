
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(64 * 64, 32) # linear layer with dim of input 1024 and output 512
        self.key = torch.nn.Linear(64 * 64, 32) # linear layer with dim of input 1024 and output 512
        self.value = torch.nn.Linear(64 * 64, 32) # linear layer with dim of input 1024 and output 512
 
        self.attn_mask = torch.nn.Parameter(torch.zeros(1, 1, 64, 64))
 
    def forward(self, qk):
        v1 = self.query(qk)
        v2 = self.key(qk)
        v3 = self.value(qk)
 
        attn_weight  = torch.softmax(v1 @ v2.transpose(-2, -1) / math.sqrt(v1.size(-1)), dim=-1) # Compute the scaled dot product of the query and key tensors 
        output = (attn_weight * v3).sum(-1)
        return output

# Initializing the model
m = Model()


# Inputs to the model
qk = torch.randn(1, 32, 64, 64)
