
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(3, 8) 
        self.key = torch.nn.Linear(3, 8)

    def forward(self, qk):
        v2 = torch.matmul(qk, self.key.weight).softmax(dim=-1) # Apply softmax to the dot product of the query and key tensors
        dropout_v2 = torch.nn.functional.dropout(v2, p=dropout_p) # Apply dropout to the softmax output
        output  = dropout_v2.matmul(self.query.weight) # Compute the dot product of the dropout output and the value tensor
        return output
# Initializing the model
m = Model()

 # Inputs to the model
qk1 = torch.randn(1, 3, 64, 64)
