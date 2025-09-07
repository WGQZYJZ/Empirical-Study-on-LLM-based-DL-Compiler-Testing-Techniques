
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(768, 384)
        self.ln1  = torch.nn.LayerNorm(384)
        self.dropout = torch.nn.Dropout2d(0.5)
        self.ln2 = torch.nn.LayerNorm(384)
 
    def forward(self, x1):
        h = x1.size(-1)  # Shape of the input tensor is [batch_size, sequence_length, features]
        q  = self.attn(x1)  # Shape is [batch_size, sequence_length, d_k]
        v  = self.attn(self.dropout(x1))  # Shape is [batch_size, sequence_length, d_v]
        k  = torch.matmul(q, v.transpose(-2, -1))  # Shape is [batch_size, sequence_length, d_k]
        scaled_k = k.div(self.scale_factor)  # Shape is [batch_size, sequence_length, d_k]
        scaled_attn = torch.nn.functional.dropout(scaled_k, p=0.5)  # Apply dropout to the scaled dot product output
        out = scaled_attn.matmul(self.value)  # Compute the dot product of the scaled and dropout output

        out = self.ln1(out + self.x1)  # Compute the new input feature vector
        return out


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(32, 64, 512)
