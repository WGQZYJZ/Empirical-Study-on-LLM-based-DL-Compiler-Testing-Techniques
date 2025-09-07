
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(20, 8)
        self.key   = torch.nn.Linear(30, 10)
        self.value = torch.nn.Linear(30, 40)
 
    def forward(self, x):
        q = self.query(x) # Compute the dot product of the query with all weights on the model
        k = self.key(x) # Compute the dot product of the key with all weights on the model
        v = self.value(x)  # Compute the dot product of the value with all weights on the model
        s1 = q.matmul(k) # Scale the dot product by the inverse scale factor
        s2 = torch.nn.functional.softmax(s1, dim=-1) # Apply softmax to the scaled dot product
        s3 = torch.nn.functional.dropout(s2, p=dropout_p)  # Apply dropout to the softmax output
        return torch.matmul(s3, v) # Compute the dot product of the dropout output and the value


# Initializing the model
m = Model()
