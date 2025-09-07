
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(8, 16)
 
    def forward(self, xq, xk, xv, mask):
        v1 = self.attn(xq, xk, xv)[0]
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(32, 8, 64, 64) # The first tensor is the query (a Tensor of shape [bsz x embed_dim x seq_len x seq_len] - where bsz stands for batch size), and the other two tensors are the keys (x_keys and x_values).
mask = torch.randint(2, 10, (32, 8, 64, 64)) > 0 # The attention mask.
