
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, inv_scale=None):

        # Compute the scaled dot product of the query and key tensors.
        scaled_dot = torch.matmul(query, key.transpose(-2,-1)) / 30
    
        # Apply the softmax function to compute the attention weights.
        weights = scaled_dot.softmax(dim=-1)
 
        # Use the attention weights to compute a weighted sum of the value tensor.
        output = weights.matmul(value)
        return output

model = ScaledDotProductAttention()

inputs  = torch.randn([8,50,4])
weights  = model(query=inputs, key=inputs, value=inputs).shape
assert str(weights) == "torch.Size([8, 26, 4])"

