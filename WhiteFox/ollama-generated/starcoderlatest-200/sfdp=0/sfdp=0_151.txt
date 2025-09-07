
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, temperature: float = 1.0):
        super().__init__()
        self.temperature = temperature
 
    def forward(self, q, k, v):
        attn = torch.matmul(q / self.temperature, k.transpose(-2, -1))
        # Convert the scaled dot product attention weights to probabilities with `softmax` and then add softmax
        probs = torch.softmax(attn, dim=-1) + 1e-6
        output = torch.matmul(probs, v)
        return output
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.key_encoder = EncoderBlock()
        self.value_encoder = EncoderBlock()
        self.scaled_dot_product_attention = ScaledDotProductAttention(temperature=1)
 
    def forward(self, q, k, v):
        # Encode the queries and keys with two different layers of encoders
        key = self.key_encoder(k)
        query = self.value_encoder(q)
 
        # Perform scaled dot product attention
        output = self.scaled_dot_product_attention(query, key, v)
 
        return output
# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
