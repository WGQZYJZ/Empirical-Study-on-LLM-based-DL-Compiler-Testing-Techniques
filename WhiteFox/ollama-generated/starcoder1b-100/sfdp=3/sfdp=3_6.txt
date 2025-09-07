
class Model(torch.nn.Module):
    def __init__(self, d_model, nhead, num_attns, ff_dim, num_hidden_layers=1):
        super().__init__()
        self.qkv = torch.nn.Linear(d_model * 3, d_model * 3) # Query and key matrix. We use the previous model
        self.layernorm1 = torch.nn.LayerNorm(d_model) 
        self.attn = torch.nn.MultiheadAttention(
            dim=d_model,
            num_heads=nhead,
            dropout=dropout_p,
        )
        self.linear = torch.nn.Linear(d_model * 3, d_model) # Linear projection for output prediction
        self.layernorm2 = torch.nn.LayerNorm(d_model) 
        self.dropout1 = torch.nn.Dropout(p=dropout_p)
        self.dropout2 = torch.nn.Dropout(p=dropout_p)
    
    def forward(self, x):
        x = self.layernorm1(x) # Normalize the input for the model
        qkv = self.qkv(x).chunk(3, dim=-1)  # Compute the hidden state matrix and query key matrix
        
        if isinstance(qkv[0], torch.nn.Tensor):
            qkv = (qkv[0].contiguous(), qkv[1].contiguous(), qkv[2].contiguous())

        attn_out, _ = self.attn(
            qkv=qkv, 
            k=x, 
            v=x, 
            mask=None if isinstance(qkv[0], torch.nn.Tensor) else x.new_zeros(*x.size()),
        ) # Attention model
        
        output = self.linear(attn_out)  # Apply linear transformation to the attention value

        output = self.layernorm2(output)  # Normalize the output for the model
        
        return self.dropout1(output), attn_out


# Initializing the model
m = Model()
x  = torch.randn(1, 64, 64, 3)
