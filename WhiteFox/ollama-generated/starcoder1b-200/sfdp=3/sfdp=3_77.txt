
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(512, 512)
        self.key = torch.nn.Linear(512, 512)
        self.value = torch.nn.Linear(512, 512)
 
    def forward(self, x1, x2):
        query = self.query(x1)  # Get the output of the first linear layer of the second input tensor
        key   = self.key(x2)    # Get the output of the first linear layer of the third input tensor
        value = self.value(x2)  # Get the output of the first linear layer of the fourth input tensor
        scaled_qk  = query.matmul(key).mul(0.1)  # Scale the dot product by a factor and then apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(scaled_qk, p=0.2) # Apply dropout to the softmax output
        out       = dropout_qk.matmul(value)    # Compute the dot product of the dropout output and the value tensor
        return out


# Initializing the model
m = Model()

