
class Model(torch.nn.Module):
    def __init__(self, d_k, d_v):
        super().__init__()
        self.d_k = d_k
        self.d_v = d_v
 
        self.W1 = torch.nn.Parameter(torch.randn(d_k, d_v))
        self.W2 = torch.nn.Parameter(torch.randn(d_v, d_k))
 
    def forward(self, x):
        batch_size = x.shape[0]
        # Compute the shape of the dot product of the query and key: (batch_size * seq_length * hidden_size)
        seq_len = x.shape[-1]
        # Shape (batch_size * seq_length, d_v)
        qk = x @ self.W2.transpose(-2, -1) / math.sqrt(x.shape[0])
        # Shape (batch_size * seq_length, d_k)
        attn_mask = torch.zeros((batch_size, seq_len), device=x.device)
        for t in range(seq_len):
            attn_mask[:, t] = 1 - math.exp(-qk[:, t].pow(-2))
        # Shape (batch_size * seq_length, d_k)
        attn_weight = torch.softmax(qk, dim=-1)
        # Shape (batch_size * seq_length, d_v)
        output = attn_weight @ x
        return output


# Initializing the model
m = Model(d_k=32, d_v=64)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
