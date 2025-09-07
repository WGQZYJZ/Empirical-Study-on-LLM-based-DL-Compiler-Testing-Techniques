
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(d_k, d_v)
 
    def forward(self, x1, x2):
        query = self.attn(x1, x2)[0]  # Compute the dot product of the query and the key
        scaled_query = query.div_(self.attn.scaling[0].unsqueeze(dim=0))  # Scale the dot product by the inverse scale factor
        softmax_query = scaled_query.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_query = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        value = self.attn(dropout_query, x2)[0]  # Compute the dot product of the dropout output and the value
        return value


# Initializing the model
m = Model()


