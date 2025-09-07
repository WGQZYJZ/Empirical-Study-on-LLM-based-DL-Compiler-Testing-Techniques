
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(10, 5) # input dimension: [batch_size, length_q, dim]
        self.key = torch.nn.Linear(20, 6)   # input dimension: [batch_size, length_k, dim]
        self.value = torch.nn.Linear(30, 7) # input dimension: [batch_size, length_v, dim]
 
    def forward(self, q, k, v):
        batch_size = q.size(0)
        q = self.query(q).view(batch_size, -1, query.shape[2])
        k = self.key(k).view(batch_size, -1, key.shape[2])
        v = self.value(v).view(batch_size, -1, value.shape[2])

        attn_mask = torch.eye(attn_mask.shape[-1]).unsqueeze(0) # [1, length_q]
        qk = q @ k.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        qk = qk + attn_mask # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result

        output = (attn_weight @ v).view(batch_size, -1, key.shape[2]) # Compute the dot product of the attention weights and the value
        return output


# Initializing the model
m = Model()

# Inputs to the model
q = torch.randn(5, 10, 64)   # input dimension: [batch_size, length_q, dim]
k = torch.randn(2, 20, 64)  # input dimension: [batch_size, length_k, dim]
v = torch.randn(3, 30, 64) # input dimension: [batch_size, length_v, dim]

