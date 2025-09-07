
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(768, 3072)
 
    def forward(self, x1):
        qk = torch.matmul(x1, x1.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk = qk / (1e-5 + torch.norm(qk, dim=-1, keepdim=True)) # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output = dropout_qk.matmul(x1) # Compute the dot product of the dropout output and the value tensor
        return output
 

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 768, 1, 1)
