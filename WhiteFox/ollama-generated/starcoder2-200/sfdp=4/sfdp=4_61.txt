
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, qk1, qk2, attn_mask):
        vq = qk1 @ qk2.transpose(-2, -1) / math.sqrt(qk1.size(-1)) + attn_mask 
        return torch.softmax(vq, dim=-1)


# Initializing the model
m  = Model()

# Inputs to the model
qk1 = torch.randn(30, 896, 768, 256) # query
qk2 = torch.randn(30, 768, 256, 896)# key
attn_mask = torch.zeros(30, 896, 768)

