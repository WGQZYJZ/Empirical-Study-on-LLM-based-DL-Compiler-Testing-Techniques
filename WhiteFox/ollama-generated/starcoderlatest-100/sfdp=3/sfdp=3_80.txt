
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk = torch.nn.Linear(d_k, d_v)
 
    def forward(self, query, key, value, scale_factor=None, dropout_p=0.1):
        qk = self.qk(torch.cat([query, key], dim=-1))  # Apply a linear transformation to concatenate the query and key vectors
        scaled_qk = qk.mul(scale_factor) # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output = dropout_qk.matmul(value)  # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()

# Inputs to the model
query, key, value = ...
scale_factor = torch.randn(())  # Scale factor is a parameter that can be learned by an optimizer for efficiency reasons. We will discuss how to do so later in this exercise
dropout_p = torch.randint(...) # Random dropout probability
