
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention_mechanism = torch.nn.MultiheadAttention(num_heads=8, input_dim=256)
 
    def forward(self, query, key, value):
        attention_output, _ = self.attention_mechanism(query, key, value, attn_mask=None, incremental_state=None, need_weights=False, need_head_weights=False)
        return attention_output


# Initializing the model
m = Model()


# Inputs to the model
query = torch.randn(128, 3, 64, 64)
key   = torch.randn(64, 10, 3, 64)
value = torch.randn(64, 10, 3, 64)


# Output of the model
