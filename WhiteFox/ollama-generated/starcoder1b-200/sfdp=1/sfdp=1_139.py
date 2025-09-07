
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.attn = torch.nn.Linear(dim, dim)
 
    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk = qk.div(torch.pow(self.scale_factor, 0.5))  # Scale the dot product by the inverse scale factor
        dropout_qk = torch.nn.functional.dropout(scaled_qk.softmax(dim=-1), p=dropout_p)  # Apply dropout to the softmax output
        attn_output = dropout_qk.matmul(value)  # Compute the dot product of the dropout output and the value tensor
        attention_weights = self.attn(attn_output).softmax(-1)  # Compute the weighted average of all key values
        context = torch.bmm(attention_weights, value)  # Use the weighted summation to compute the new context
        return context


# Initializing the model
model = Model(8)

# Inputs to the model
query = torch.randn(2, 3, 64, 64)
key = torch.randn(2, 3, 64, 64)
value = torch.randn(2, 3, 64, 64)
