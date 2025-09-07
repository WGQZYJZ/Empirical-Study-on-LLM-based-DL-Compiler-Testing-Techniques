
class AttentionModule(torch.nn.Module):
    def __init__(self, d_k, nhead, dropout=0.1):
        super().__init__()
        self.d_k = d_k
        self.nhead = nhead
        self.wqs = torch.nn.Linear(d_model, 3 * nhead)
        self.wqks = torch.nn.Linear(d_model, 3 * nhead)
        self.proj = torch.nn.Linear(d_model, d_model)
        self.dropout = torch.nn.Dropout(dropout)
 
    def forward(self, q, k, v):
        # Calculate the scaled dot product between query and key. This is the scaled attention weights.
        qks = self.wqs(q).view(-1, self.nhead, 3).transpose(-2, -1)
        qk_weights = (qks @ k.transpose(-2, -1)) / math.sqrt(self.d_model ** 0.5)
 
        # Add the attention mask to scaled dot product
        qk_weights += attn_mask
 
        # Apply softmax to get the weights for each head's output
        qk_weights = torch.softmax(qk_weights, dim=-1)
 
        # Dropout operation before calculating attention
        qk_weights = self.dropout(qk_weights)
 
        # Calculate the output based on the weights and values
        output = (qk_weights @ v).transpose(-2, -1).contiguous()
        output = output.view(-1, 3 * nhead)
 
        # Project to match the dimensionality of value (only in the last two dimensions for now)
        attn = self.proj(output).transpose(-2, -1)

        return qk_weights, attn

# Initializing the model
a = AttentionModule()

# Inputs to the model
q = torch.randn(1, 3, d_model) # Query
k = torch.randn(1, 3, d_model) # Key
v = torch.randn(1, 3, d_model) # Value
qk_weights, attn = a(q, k, v)


# Description of requirements
Please generate all the tests to ensure that `q` is multiplied by 0.5 before feeding it to the dot product operator; `k` and `v` are added to the dot product before applying softmax; after computing the attention weights for query-key pairs, `qk_weights` should be divided by the length of each key (which is equal to its sequence length). Then, use the result of the dot product (`output`) as input for the fully connected layer in the attention block.

