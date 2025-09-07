
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(2048, 512) # Linear layer that computes the dot product of the query and key, which can then be multiplied by the attention mask to prevent certain positions from being attended to.
        self.key   = torch.nn.Linear(2048, 512)
        self.value = torch.nn.Linear(2048, 512)
 
    def forward(self, query, key, value, mask):
        qk = self.query(query) @ self.key.transpose(-2,-1).float() / math.sqrt(2048) # Compute the dot product of the query and key, and scale it
        qk += (mask == 0).unsqueeze(1).unsqueeze(2).type_as(qk) * -9e6  # Add the attention mask to the scaled dot product, which will be used to prevent certain positions from being attended to.
        return self.value(torch.softmax(qk, dim=-1)) @ torch.transpose(self.key, -2,-1).float()


# Initializing the model
m = Attention()

# Inputs to the model
x  = torch.randn(4, 80, 56) # shape (batch_size, seq_len, embedding_dim), where embedding_dim is usually set as 512 or 768.
y  = torch.randn(3, 80, 56) # shape (batch_size, seq_len, embedding_dim).
mask = torch.rand(*x.shape[:2], dtype=torch.float) > 0.5  # shape (seq_len1, seq_len2), where both values are set to 0 or 1 randomly.
