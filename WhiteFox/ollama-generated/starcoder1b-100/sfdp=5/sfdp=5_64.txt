
class Model(torch.nn.Module):
    def __init__(self, input_dim, hidden_dim, depth):
        super().__init__()
        self.attn = MultiHeadAttention(input_dim, hidden_dim)
        self.ln1 = torch.nn.LayerNorm(hidden_dim)  # Add layer normalization after each convolution in the encoder
        self.ln2 = torch.nn.LayerNorm(hidden_dim)  # Add layer normalization after each pointwise convolution in the encoder
        self.fc1 = torch.nn.Linear(input_dim, hidden_dim)
        self.fc2 = torch.nn.Linear(hidden_dim * depth, hidden_dim)
        self.ln3 = torch.nn.LayerNorm(hidden_dim)
        self.ln4 = torch.nn.LayerNorm(hidden_dim)
 
    def forward(self, x):
        # Query the encoder with both query and key
        q = self.attn(x, x, x)  # First convolutions compute the dot product of the encoder outputs. We add the attention mask to make sure that only information related to the input is used for subsequent computation.
        k = self.attn(x, x, x)
 
        # Compute layer normalization after each convolution
        q *= torch.tanh(self.ln1(self.fc1(x)))  # Add skip connection to make it possible to have multiple attention heads per node in the transformer.
        k *= torch.tanh(self.ln2(self.fc2(x)))
 
        output = torch.cat([q, k], dim=1)
        output = torch.tanh(self.ln3(self.fc2(output)))  # Add layer normalization after the first two convolutions
        output = torch.mul(output, self.attn_mask)  # Compute dot product of attention weights and input
 
        return output


# Initializing the model
m = Model(input_dim=128, hidden_dim=512, depth=3)


