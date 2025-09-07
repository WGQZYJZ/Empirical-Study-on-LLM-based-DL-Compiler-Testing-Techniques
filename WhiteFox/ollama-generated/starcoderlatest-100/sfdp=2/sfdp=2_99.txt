
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.Linear(768, 256)
 
    def forward(self, query, key, value, inv_scale_factor, dropout_p):
        qk = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and the key
        scaled_qk = qk.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk.matmul(value) # Compute the dot product of the dropout output and the value
        return output


# Inputs to the model
query = torch.randn(1024, 768)
key = torch.randn(1024, 768)
value = torch.randn(1024, 768)
inv_scale_factor = np.array([9,9,1]).reshape(3,-1).astype(np.float32)
dropout_p = 0.5
attention_out  = Attention()(query, key, value, inv_scale_factor, dropout_p)


# User: What is the shape of the output tensor? Is it consistent with the description of requirements for the new model?



def check(output):
    assert torch.all(torch.eq(attention_out.shape, output.shape))
    # ...



