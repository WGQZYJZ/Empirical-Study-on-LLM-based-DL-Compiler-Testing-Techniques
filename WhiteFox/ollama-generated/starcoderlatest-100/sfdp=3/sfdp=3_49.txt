
class Model(torch.nn.Module):
    def __init__(self, d_model, d_head=8, d_inner=2048):
        super().__init__()

        self.ln_q = torch.nn.LayerNorm(d_model)
        self.ln_k = torch.nn.LayerNorm(d_model)
        self.ln_v = torch.nn.LayerNorm(d_model)
 
        self.attn = torch.nn.MultiheadAttention(d_model, num_heads=d_head)
        self.mlp = torch.nn.Sequential(
            torch.nn.Linear(d_model * 2, d_inner),
            torch.nn.ReLU(),
            torch.nn.Linear(d_inner, d_model),
        )
 
    def forward(self, x):
        q = self.ln_q(x)
        k = self.ln_k(x)
        v = self.ln_v(x)

        # Compute the dot product of the query and key tensors
        qk = torch.matmul(q, k.transpose(-2, -1))
 
        # Scale the dot product by a factor
        scaled_qk = qk.mul(scale_factor)
 
        # Apply softmax to the scaled dot product
        softmax_qk = scaled_qk.softmax(dim=-1)
 
        # Apply dropout to the softmax output
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)

        # Compute the dot product of the dropout output and the value tensor
        output = self.attn(x, x, x)[0] + dropout_qk.matmul(v)
 
        # MLP for intermediate heads
        return self.mlp(torch.cat((output, q), dim=1))

# Initializing the model
m = Model(32)


