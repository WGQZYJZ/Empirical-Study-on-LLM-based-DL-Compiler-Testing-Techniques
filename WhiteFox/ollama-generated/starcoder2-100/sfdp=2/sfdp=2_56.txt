
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(64, 8)
 
    def forward(self, q1, k1=None, v1=None, scale_factor=-1e-5):
        if not (k1 is None or v1 is None):
            attn_output, _ = self.attn(q1, k1, v1)
        else: 
            attn_output, _ = self.attn(q1, q1, q1)

        return attn_output


# Initializing the model
m  = Model()

# Inputs to the model