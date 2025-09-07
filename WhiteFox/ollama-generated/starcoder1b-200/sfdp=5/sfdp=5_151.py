
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.ln  = torch.nn.LayerNorm([8], eps=1e-05)
 
    def forward(self, x):
        v = self.conv(x)
        v = self.ln(v)
        v = self.dropout(v, training=False) # Apply dropout to the input
        v = torch.matmul(v, self.key)  # Compute the dot product of the input and the key (with scaling by sqrt(d_k))
        attn_weight = torch.softmax(v, dim=-1)  # Apply softmax to the result
        output = torch.matmul(attn_weight, self.value)  # Compute the dot product of the output and the value
        return output


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)  # Batch size 2, 3 channels 64*64 (the dimension of the input and the number of features in the convolution layer)
y1 = m(x1)   # Compute y1

