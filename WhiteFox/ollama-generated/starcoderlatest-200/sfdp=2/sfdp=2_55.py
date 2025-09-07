
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(1024, 32)
 
    def forward(self, qk_scaled, v):
        output = self.attention(qk_scaled, v)[0]
        return output


# Inputs to the model
qk_scaled = torch.randn(16, 32, 128) # The query, key and value are scaled by a separate inverse scale factor
v = torch.randn(16, 4096, 512) # The queries, keys and values in the decoder layer are all input values
