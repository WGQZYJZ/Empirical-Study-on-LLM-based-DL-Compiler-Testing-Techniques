
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(8, 4)
        self.key   = torch.nn.Linear(8, 4)
 
    def forward(self, x1):
        qk = torch.matmul(x1, self.query.weight)
        k  = torch.matmul(x1, self.key.weight)
        k  = k / math.sqrt(k.size(-1).float() * k.size(-1))
        attn_weights  = scaled_softmax - (scaled_softmax @ k.transpose(-2, -1))
        dropout_attn_weights = torch.nn.functional.dropout(attn_weights, p=dropout_p)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
