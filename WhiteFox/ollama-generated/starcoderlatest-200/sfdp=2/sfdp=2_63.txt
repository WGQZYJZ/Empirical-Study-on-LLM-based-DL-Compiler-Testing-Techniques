
class Model(torch.nn.Module):
    def __init__(self, d_model=64, nhead=10, hidden_dim=256, num_layers=4):
        super().__init__()

        # Layer 1
        self.layernorm_q = torch.nn.LayerNorm(d_model)
        self.attn = MultiHeadAttention(
            d_model, nhead, dropout_p=0.3, bias=True
        )

        # Layer 2
        self.layernorm_k = torch.nn.LayerNorm(d_model)
        self.attn2 = MultiHeadAttention(
            d_model, nhead, dropout_p=0.3, bias=True
        )

        # Output layer
        self.dense = torch.nn.Linear(hidden_dim, d_model)
        self.layernorm = torch.nn.LayerNorm(d_model)

    def forward(self, x):
        # Layer 1
        q = self.layernorm_q(x)
        k = self.layernorm_k(x)

        attn_output, _ = self.attn(q, k, v=None)
        output = attn_output + x
        
        # Layer 2
        q = self.layernorm_q(output)
        k = self.layernorm_k(output)

        attn_output, _ = self.attn2(q, k, v=None)
        output = attn_output + output

        # Output layer
        x = self.dense(output)
        x = self.layernorm(x)

        return x


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
