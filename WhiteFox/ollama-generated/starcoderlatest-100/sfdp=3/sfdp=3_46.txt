
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(
            dim_per_head=128, # Dimension for each head (i.e., number of channels per head). The dimension must be specified when creating a linear layer with nn.Linear function to compute the dot product between the query and key tensors. 
            num_heads=4, # Number of heads in self-attention mechanism.
            dropout_p=0.1)  # Dropout probability for attention mechanism

    def forward(self, qk):
        output = self.attention(qk[0], qk[1], v=qk[2])
        return output


# Initializing the model
m = Model()

# Inputs to the model
x_qk = torch.randn(2, 3, 8, 64) # [num_layers * num_heads, batch, sequence_length, head_dim]
