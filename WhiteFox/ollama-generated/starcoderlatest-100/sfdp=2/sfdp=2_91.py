
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention_dropout = torch.nn.Dropout(attention_dropout)
        self.attention_softmax = torch.nn.Softmax(dim=-1)
        self.linear = torch.nn.Linear(hidden_size * 2, intermediate_size)
 
    def forward(self, qk):
        # Compute the dot product of query and key with attention dropout
        v = qk.matmul(v)
        # Scale the output by sqrt(inverse scale factor)
        v = v / math.sqrt(scale_factor)
        # Softmax to normalize the output
        v = self.attention_softmax(v)
        # Apply dropout to compute the output of attention with attention dropout
        v = self.attention_dropout(v)
        # Compute output of linear projection
        v = v.matmul(self.linear.weight.t())
        return v


# Initializing the model
m = Model()

# Query tensor
query  = torch.randn(batch_size, embedding_dim, query_length)

# Key tensor
key  = torch.randn(batch_size, embedding_dim, key_length)

# Scale factor to compute output of linear projection
scale_factor = torch.sqrt((torch.ones(batch_size)*scale_dropout).to(device))

# Inverse scale factor to normalize the dot product of query and key
inv_scale_factor  = 1 / scale_factor

