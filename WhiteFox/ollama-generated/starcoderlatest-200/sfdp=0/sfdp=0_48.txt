
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(4096, 32) # (bsz, 768) -> (bsz, 32)
        self.activation = torch.nn.GELU() # GELU activation to the output of linear layer
        self.linear2 = torch.nn.Linear(32, 512) # (bsz, 32) -> (bsz, 512)
        self.dropout = torch.nn.Dropout(0.1)
 
    def forward(self, x):
        y  = self.linear1(x)
        v1 = self.activation(y)
        y  = self.linear2(v1)
        v2 = self.dropout(y)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
q = torch.randn(1, 4096, 768) # (bsz, 4096, d_k) -> (bsz, 32)
k = torch.randn(1, 4096, 768) # (bsz, 4096, d_k) -> (bsz, 512)
v = torch.randn(1, 4096, 768) # (bsz, 4096, d_v) -> (bsz, 512)
scaled_dot_product = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(k.size(-1))


# Calculating the attention weights and then weighted sum
attention_weights = scaled_dot_product.softmax(dim=-1) # (bsz, nheads, length_q, length_kv) -> (bsz, 128, length_q, length_kv)
output = torch.matmul(attention_weights, v) # (bsz, 128, length_q, length_kv) -> (bsz, 512, length_q, length_v)

