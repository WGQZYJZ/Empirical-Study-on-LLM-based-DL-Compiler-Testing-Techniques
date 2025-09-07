
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(16, 32) # Embedding layer with a dimension of 16 is used to transform the hidden states of the query and key
        self.key   = torch.nn.Linear(16, 32)
        self.value = torch.nn.Linear(16, 32)
 
    def forward(self, x1):
        qk = torch.matmul(x1, self.query.weight.transpose(-2, -1)) / math.sqrt(self.query.in_features) # Compute the dot product of the query and key, and scale it
        qk += self.key_padding_mask  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True) # Apply dropout to the softmax output
        output = torch.matmul(attn_weight, self.value.weight) # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(16, 24, 32, 32)
