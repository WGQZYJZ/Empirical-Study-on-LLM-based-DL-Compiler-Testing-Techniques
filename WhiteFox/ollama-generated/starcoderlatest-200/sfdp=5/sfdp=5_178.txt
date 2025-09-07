
class Model(torch.nn.Module):
    def __init__(self, num_heads=1, use_attn_mask=False):
        super().__init__()
        self.num_heads = num_heads
        self.use_attn_mask = use_attn_mask
        self.attn_proj = torch.nn.Linear(768, 32)
        self.value_proj = torch.nn.Linear(1024, 768)
 
    def forward(self, x):
        qk = x @ self.q_proj.transpose(-1, -2).unsqueeze(-2) / math.sqrt(x.size(-1)) # Compute the dot product of the query and key, and scale it
        if self.use_attn_mask:
            attn_mask = torch.nn.functional.softmax(qk, dim=-1) # Apply softmax to the result
            attn_weight = (attn_mask @ self.v_proj).mean(-2).unsqueeze(-1) # Compute a weighted average of all values in each attention head
        else:
            attn_weight = torch.nn.functional.softmax(qk, dim=-1)  # Apply softmax to the result

        output = (attn_weight @ self.v_proj).mean(-2).unsqueeze(-1)  # Compute a weighted average of all values in each attention head
        return output


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(4, 768, 30, 40)
