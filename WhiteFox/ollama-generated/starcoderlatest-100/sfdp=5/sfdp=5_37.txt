
class AttentionModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(256, 32)
        self.key = torch.nn.Linear(256, 32)
        self.value = torch.nn.Linear(256, 32)
 
    def forward(self, x1):
        query_v1 = self.query(x1) # Get the output of the linear layer with input `x1` and output size 16
        key_v1 = self.key(x1) # Get the output of the linear layer with input `x1` and output size 16
        value_v1 = self.value(x1) # Get the output of the linear layer with input `x1` and output size 16
        qk = torch.matmul(query_v1, key_v1.transpose(-2, -1)) # Compute the dot product of query_v1 with itself, to be added in the attention mask computation, and scale it
        qk += attn_mask # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True) # Apply dropout to the softmax output
        output = torch.matmul(attn_weight, value_v1) # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m = AttentionModel()

# Inputs to the model
x1 = torch.randn(1, 256, 1, 1)
