
class Model(torch.nn.Module):
    def __init__(self, n_head=8, d_key=64, d_model=64, dropout=0):
        super().__init__()
        self.attention = torch.nn.Linear(d_key, n_head * d_key)
        self.dropout = torch.nn.Dropout(dropout)
        self.linear  = torch.nn.Linear(n_head * d_key, d_model)
 
    def forward(self, x1):
        # Initialize the key tensor
        k1 = x1 @ self.attention.weight[:, :, None] / math.sqrt(x1.size(-2))  # Compute the dot product of the query and key, and scale it
        k1 = k1 + self.attention.bias[:, :, None]  # Add the bias for the attention weights
        k1 = self.dropout(k1)  # Dropout layer to prevent vanishing / exploding gradients during training
        # Initialize the value tensor
        v = x1 @ self.attention.weight[:, None, :] / math.sqrt(x1.size(-2))  # Compute the dot product of the query and key, and scale it
        v = v + self.attention.bias[:, None, :]  # Add the bias for the attention weights
        v = self.dropout(v)  # Dropout layer to prevent vanishing / exploding gradients during training
        # Compute the weighted sum of the value and the attention weights
        x  = torch.matmul(k1, v) * self.attention.weight[:, :, None]  # Dot-product formula for scaled dot product
        # Perform the output projection
        x  = torch.cat([x, self.linear(x)], dim=-2)
        return x


# Initializing the model
m  = Model()


