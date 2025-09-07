
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(3, 4)
        self.key = torch.nn.Linear(4, 5)
        self.value = torch.nn.Linear(5, 6)
 
    def forward(self, query_input, key_input, value_input):
        vq = self.query(query_input).unsqueeze(-1) * self.key(key_input).unsqueeze(0).transpose(-2, -1) / math.sqrt(key_input.size(-1)) + 1e-6 # Compute the dot product of the query and key, and scale it
        qk = vq @ value_input.transpose(-1, -2) / math.sqrt(value_input.size(-1))  # Compute the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight * value_input  # Compute the dot product of the attention weights and the value
        return output


# Initializing the model
m = Model()

