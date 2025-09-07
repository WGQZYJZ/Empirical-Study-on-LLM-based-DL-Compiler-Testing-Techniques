
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, qk1, v1):
        query  = torch.einsum('b c h w, b d h w -> b d c', [qk1, k]) # Query is transposed from the previous example in this pattern
        attention_weights = torch.softmax(scaled_dot_product)  # Softmax normalization and apply to the dot product
        value = torch.einsum('b d c, b d h w -> b c h w', [attention_weights, v1])  # Einstein summation is used here as well
 
        return output

# Initializing the model
m = Model()

# Inputs to the model
qk1 = torch.randn(1, 3, 64, 64)  # Query Tensor has shape (1, 8, 64, 64)
v1 = torch.randn(1, 128, 64, 64)  # Value Tensor has shape (1, 8, 64, 64)
