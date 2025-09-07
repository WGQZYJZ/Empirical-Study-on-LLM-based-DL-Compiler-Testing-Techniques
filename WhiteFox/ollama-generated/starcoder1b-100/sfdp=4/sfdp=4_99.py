
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(3, 8)
        self.key   = torch.nn.Linear(3, 16)

    def forward(self, x1, x2):
        vq  = self.query(x1).view(-1, 8, 1, 1) # Compute the query weights
        vk  = self.key(x2).transpose(1, -2) # Compute the key weights and transpose them to form a spatial grid of values (n_heads * k_dim = n_layers * k_dim, k_dim is the number of units in the hidden state)
        vqk  = torch.bmm(vq, vk) # Compute the value-query weights using broadcast multiplication
        attn_weight = torch.softmax(vqk, dim=-1).view(-1, 8)  # Apply softmax to the result

        v  = self.value(x2).transpose(0, 1) # Compute the value weigts and transpose them to form a spatial grid of values (n_layers * k_dim = n_heads * k_dim, k_dim is the number of units in the hidden state)
        output = attn_weight @ v  # Apply the weighted sum to the outputs
        return output


# Initializing the model
m = Model()


