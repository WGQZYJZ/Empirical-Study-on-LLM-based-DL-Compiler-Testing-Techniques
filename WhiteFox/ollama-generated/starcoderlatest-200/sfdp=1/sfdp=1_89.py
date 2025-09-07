
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(8, 16)
 
    def forward(self, qk, v):
        attn_output, _ = self.attn(qk, k=qk, v=v) # This is the call to the attention module 
        return attn_output


# Initializing the model
m = Model()

