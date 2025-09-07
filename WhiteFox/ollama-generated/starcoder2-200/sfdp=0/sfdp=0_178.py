
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, config):
        super().__init__()
        self.config  = config
 
        dim  = self.config['hidden'] // self.config['num_heads']
 
        self.toqkv  = torch.nn.Linear(dim, dim * 3)
        self.toout  = torch.nn.Linear(dim, dim)
 
    def forward(self, hidden_states):

        # Split the query/key/value inputs into their respective heads.
        query_hidden_states, key_hidden_states, value_hidden_states  = (torch.chunk(self.toqkv(hidden_states).squeeze(), 3))
 
        # Compute the scaled dot-product attention weights using the query and key hidden states.
        attention_weights = torch.matmul(query_hidden_states, key_hidden_states[0].permute(-1, -2)) / self.config['scale']
 
        # Normalize the attention weights to compute softmax.
        attention_weights  = attention_weights.softmax(dim=-1)
 
        # Apply the attention weights to the value hidden states and concatenate them together.
        output  = torch.matmul(attention_weights, value_hidden_states).squeeze(-2)
 
        # Pass the resulting concatenation through a feed-forward layer with ReLU activation.
        output = F.relu(self.toout(output))
 
        return output

m = ScaledDotProductAttention()
__output__  = m(x1)

