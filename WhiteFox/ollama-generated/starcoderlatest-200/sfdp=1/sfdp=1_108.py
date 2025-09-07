
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(3, 8, num_heads=1)
 
    def forward(self, x1, x2):
        v1, v2 = self.attention(x1, key_padding_mask=torch.tensor([[False, True]])) # Use the first value tensor as the query in multihead attention with the second value tensor as the key
        v3 = torch.nn.functional.interpolate(v1, scale_factor=2) # Interpolate the output of the multihead attention to the scaled input size
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 3, 128, 128)
