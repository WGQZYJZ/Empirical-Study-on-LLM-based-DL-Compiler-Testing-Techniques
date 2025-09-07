
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(512, 8)
 
    def forward(self, query, key, value):
        v1  = query @ key.transpose(-2, -1) / math.sqrt(d_model) # Compute the dot product of a query and a key
        v2  = F.normalize(v1).div_(scale)                              # Scale the dot product by the square root of the model depth
        v3  = torch.softmax(v2, dim=-1)                                  # Apply softmax to the dot product
        v4  = torch.dropout(v3, p=dropout_p)                                # Apply dropout to the softmax output
        v5  = (v4 @ value).transpose(-2, -1)                              # Compute the dot product of the softmax output and a value
        return self.linear(v5)                                           


# Initializing the model
m = Model()


# Inputs to the model
query   = torch.randn(64, 32, d_model).unsqueeze(1) # (batch_size x nhead x seq_len x head_dim)
key     = torch.randn(64, 32, d_model).unsqueeze(0) # (batch_size x nhead x seq_len x head_dim)
value   = torch.randn(64, 32, d_model).unsqueeze(0) # (batch_size x nhead x seq_len x head_dim)
