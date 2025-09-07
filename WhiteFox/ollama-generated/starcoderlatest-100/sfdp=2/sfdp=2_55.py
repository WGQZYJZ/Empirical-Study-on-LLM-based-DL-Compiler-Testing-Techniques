
class AttentionModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(5, 10)
 
    def forward(self, x1):
        qk = torch.matmul(x1, x2.transpose(-2, -1)) # Compute the dot product of the query and key
        scaled_qk = qk.div(scale_factor)   # Scale the dot product by the scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5) # Apply dropout to the softmax output
        output = dropout_qk.matmul(v)        # Compute the dot product of the dropout output and the value
        return v6
# Initializing the model
m2 = AttentionModel()

