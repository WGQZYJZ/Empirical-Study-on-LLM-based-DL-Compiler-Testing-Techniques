
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        query  = torch.matmul(x1, x2.transpose(-2, -1)) # Compute the dot product of the query and the key
        scaled_qk  = query.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk.matmul(x2) # Compute the dot product of the dropout output and the value
        return output


# Inputs to the model
query  = torch.randn(8, 32, 64, 64) # query shape (batch size x hidden_size x seq len x dim)
key  = torch.randn(32, 128, 64, 64) # key shape (batch size x hidden_size x seq len x dim)


