
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(10, 20)
        self.key = torch.nn.Linear(20, 40)
        self.value = torch.nn.Linear(40, 60)
 
    def forward(self, x1, x2):
        qk = torch.matmul(x1, self.query)  # Compute the dot product of the query and the key
        v = self.value(x2)  # Extract the value
        sqk = torch.nn.functional.softmax(qk, dim=-1)  # Apply softmax to the scaled dot product
        dk = torch.matmul(skq, self.key.transpose(-2, -1))  # Compute the dot product of the dropout output and the key
        d = torch.nn.functional.dropout(dk, p=0.2)  # Apply dropout to the softmax output
        y = d.matmul(v)  # Compute the dot product of the dropout output and the value
        return y


# Initializing the model
m = Model()


