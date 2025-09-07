
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, attn_mask=None):
        # ...  Compute the dot product of the query and key tensors...
        # ...  Add the attention mask to the scaled dot product...
        # ... Apply softmax to the result ...

        # ...  Compute the dot product of the attention weights and the value tensor ...

# Initializing the model
attn = ScaledDotProductAttention()


