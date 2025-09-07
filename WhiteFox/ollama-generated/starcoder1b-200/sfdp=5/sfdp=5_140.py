
class Model(torch.nn.Module):
    def __init__(self, d_model, nhead):
        super().__init__()
        self.attn = torch.nn.Linear(d_model, d_model)
        self.linear = torch.nn.Linear(d_model, d_model)
 
    def forward(self, query, key, value):
        kdim = self.attn._parameters['weight'].size(-1)  # Get the number of input dimensions of the attention weight matrix
        q = query.view(*query.shape[:-1], -1)  # Convert the query to a vector with shape (batch_size, seq_len, num_heads, depth), where each element in the query is a time step at every attention head
        v = value.view(-1, kdim)  # Create a vector of vectors that has size (seq_len * num_heads, depth)
        v = self.attn(v).transpose(-2, -1)  # Convert the output of the attention mechanism to a matrix with shape (seq_len * num_heads, batch_size, depth) and transpose it. This is required for the attention computation.
        v = torch.dropout(v, p=self.dropout, train=self.training)
        o = self.linear(torch.cat((q, v), dim=-1))  # Add the two vectors and normalize them
        o = F.softmax(o, dim=-1).type_as(o)  # Apply softmax to the attention weights matrix
        return o


# Initializing the model
m  = Model()


