
class Model(torch.nn.Module):
    def __init__(self, hidden_dim, num_attention_heads):
        super().__init__()
        self.hidden_dim = hidden_dim  # Number of hidden units in the transformer block
        self.num_attention_heads = num_attention_heads  # Number of attention heads

        self.query = torch.nn.Linear(self.hidden_dim, self.hidden_dim)
        self.key = torch.nn.Linear(self.hidden_dim, self.hidden_dim)
        self.value = torch.nn.Linear(self.hidden_dim, self.hidden_dim)

        # We use 128-dimensional keys because that's the largest one in the paper.
        self.query = nn.Parameter(torch.randn(1, hidden_dim, hidden_dim))
        self.key = nn.Parameter(torch.randn(1, num_attention_heads, hidden_dim, hidden_dim))
        self.value = nn.Parameter(torch.randn(1, num_attention_heads, hidden_dim, hidden_dim))

        # Initialize attention mask to 1.0 for all elements except the last element which is -1.0
        self.attn_mask = torch.ones(1, num_attention_heads, 1, 1)
        self.attn_mask[0][:, 0] = -1e5

    def forward(self, x):
        query = self.query(x).chunk(2, dim=-1)  # Split the input into query and key components
        value = self.value(x).chunk(2, dim=-1)  # Split the input into query and key components

        # Compute attention
        q = torch.cat([q0, q1], dim=1)  # Concatenate keys with their corresponding values to compute Q
        attn = torch.matmul(q, self.key) / math.sqrt(self.hidden_dim)  # Compute the scaled dot product of the query and key matrix (divide by sqrt of dimension to prevent division by zero)
        attn = torch.dropout(attn, dropout_p, True)

        # Apply softmax on Q and scale to the value output, then return the output value
        attn_weight = torch.softmax(attn, dim=-1)  # Use Softmax to get weights between query and key component (weights are sum of queries and keys)
        attn_value = torch.matmul(attn_weight, value) / math.sqrt(self.hidden_dim)  # Get the dot product of these attention weights with the value matrix to get the final output
        output = torch.cat([q0, attn_value], dim=1)

        return output

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
