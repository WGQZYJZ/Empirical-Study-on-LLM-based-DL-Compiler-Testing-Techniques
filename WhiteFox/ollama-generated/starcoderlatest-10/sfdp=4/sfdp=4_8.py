
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(2048, 1024)
        self.key   = torch.nn.Linear(2048, 1024)
        self.value = torch.nn.Linear(2048, 1024)
 
    def forward(self, q_input, k_input):
        qk  = torch.bmm(q_input, k_input.transpose(-2, -1)) / math.sqrt(q_input.size(-1)) # Compute the dot product of the query and key, and scale it
        attn_mask = torch.ones(qk.shape).to(qk.device) # Attention mask for invalid positions

        qk  = qk + attn_mask 
        attn_weights = torch.softmax(qk, dim=-1) # Apply softmax to the result

        output = torch.bmm(attn_weights, self.value) # Compute the dot product of the attention weights and the value
        return output


# Initializing the model
m = Model()

# Inputs to the model
q_input = torch.randn(1, 2048, 512, 16)
k_input = torch.randn(1, 2048, 512, 16)
