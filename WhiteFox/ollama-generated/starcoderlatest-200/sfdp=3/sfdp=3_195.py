
class Model(torch.nn.Module):
    def __init__(self, heads=4):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(
            embed_dim=32, 
            num_heads=4,
            kdim=None, vdim=None
        )
 
    def forward(self, qk, value):
        attention_output, attention_weights = self.attention(qk, value)  # Apply attention with scaled dot-product key/values and attention mask (if there is one)
        return attention_output


# Initializing the model
m = Model()

