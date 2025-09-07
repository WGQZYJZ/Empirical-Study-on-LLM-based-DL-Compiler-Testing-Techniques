
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(10, 2)  # Query layer
        self.key = torch.nn.Linear(10, 4)   # Key layer
        self.value = torch.nn.Linear(5, 8)   # Value layer
 
    def forward(self, x1):
        k = self.query(x1)
        v = self.value(x1)
        qv = torch.matmul(k, v)  # Compute the dot product of the query and key tensors
        return torch.nn.functional.dropout(qv, p=dropout_p)


# Inputs to the model
query  = torch.randn(3, 4)      # Input tensor for the attention model
key     = torch.randn(3, 5)      # The same input for the attention model
value   = torch.randn(10, 2)    # The same input for the attention model
