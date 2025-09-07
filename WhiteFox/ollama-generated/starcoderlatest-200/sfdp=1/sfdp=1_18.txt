
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(8, 4)
 
    def forward(self, x1, key):
        qk = torch.matmul(x1, key.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk = qk / math.sqrt(key.shape[-1])  # Scale the dot product by an inverse square root to normalize it

        attention = self.attention(scaled_qk)  # Apply multihead attention to the scaled dot product
        output = attention[0] + attention[1]  # Add the output of the first multihead attention layer and the second multihead attention layer
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(8, 64, 64)
key = torch.randn(256, 3, 64, 64)
