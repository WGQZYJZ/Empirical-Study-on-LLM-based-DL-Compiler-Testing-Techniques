
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention()
 
    def forward(self, query, key, value):
        scaled_qk = self.attention(query, key, value)  # Compute the dot product of the query and key tensors
        softmax_qk = scaled_qk / math.sqrt(scaled_qk.size(-1))  # Apply softmax to the scaled dot product
        output = torch.nn.functional.dropout(softmax_qk, p=0.4) # Apply dropout to the softmax output
        return self.attention
# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(16, 32, 64, 64)
key   = torch.randn(16, 32, 64, 64)
value = torch.randn(16, 32, 64, 64)
