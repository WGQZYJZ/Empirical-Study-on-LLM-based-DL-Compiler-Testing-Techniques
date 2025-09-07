
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(num_heads=8,  # number of heads
                                                     input_dim=16)    # dimension of each head

    def forward(self, qk, key, value):
        scaled_qk = qk / (0.5 * inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)  # apply softmax to the dot product

        return self.attention(qk, key, value, attention_mask=softmax_qk)[0]


# Initializing the model
m = Model()

# Inputs to the model
qk = torch.randn(16, 32, 192, 16) # shape [batch size, seq len q, num heads k, head dim v]
key = torch.randn(16, 32, 192, 64) # shape [batch size, seq len k, num heads k, head dim v]
value = torch.randn(16, 32, 192, 64) # shape [batch size, seq len v, num heads k, head dim v]
