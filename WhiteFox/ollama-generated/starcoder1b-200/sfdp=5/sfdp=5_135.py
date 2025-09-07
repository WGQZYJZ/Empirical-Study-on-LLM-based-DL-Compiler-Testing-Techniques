
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer_norm = torch.nn.LayerNorm((512,))  # The size of the input must be divisible by `attn_size`.
        self.dropout = torch.nn.Dropout(0.1)
        self.linear_q = torch.nn.Linear((512,), (512//8))
        self.linear_k = torch.nn.Linear((512,), (512//8))
        self.linear_v = torch.nn.Linear((512,), (512//8))
 
    def forward(self, x, k, v):
        query  = self.linear_q(x)  # The size of the query must be divisible by `attn_size`.
        key     = self.linear_k(k)
        value   = self.linear_v(v)
        output  = (query @ key.transpose(-2, -1)) / math.sqrt((key.size(-2)*key.size(-1)))  # Compute the dot product of the query and key, and scale it
        output  = output + x[:, None] * torch.eye(k.shape[-1], device=x.device)  # Add the bias to the attention mask
        attn_weight = torch.softmax(output, dim=-1)  # Apply softmax to the result
        attn_weight = self.dropout(attn_weight, dropout_p, True)  # Apply dropout to the softmax output
        return (attn_weight @ value).transpose(-2, -1)

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 16, 16)
