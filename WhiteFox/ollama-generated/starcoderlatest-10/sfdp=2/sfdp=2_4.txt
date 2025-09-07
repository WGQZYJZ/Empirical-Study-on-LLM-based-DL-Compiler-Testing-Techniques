
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, qk1):
        qk2 = torch.matmul(qk1[0], qk1[1].transpose(-2, -1)) # Compute the dot product of query and key
        scaled_qk2 = qk2.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk2 = scaled_qk2.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk2 = torch.nn.functional.dropout(softmax_qk2, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk2.matmul(qk1[1]) # Compute the dot product of the dropout output and the key
        return qk2
# Initializing the model
m = Model()

# Query and keys to the model
qk1 = (torch.randn(3, 8), torch.randn(3, 4))
