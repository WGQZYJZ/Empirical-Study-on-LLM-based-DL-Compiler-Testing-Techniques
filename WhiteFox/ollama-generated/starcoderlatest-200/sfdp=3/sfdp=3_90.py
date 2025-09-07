
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(768, 384)
        self.key   = torch.nn.Linear(768, 384)
        self.value = torch.nn.Linear(768, 384)
 
    def forward(self, x1):
        v1 = torch.matmul(x1, self.query.weight) # Compute the dot product of the query and key tensors
        v2 = self.key(x1).transpose(-2,-1) * v1 # Scale the dot product by a factor
        softmax_v2 = v2.softmax(-1) # Apply softmax to the scaled dot product
        dropout_v2 = torch.nn.functional.dropout(softmax_v2, p=0.1) # Apply dropout to the softmax output
        return (dropout_v2 @ self.value(x1)).transpose(-2,-1) # Compute the dot product of the dropout output and the value tensor


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 768)
