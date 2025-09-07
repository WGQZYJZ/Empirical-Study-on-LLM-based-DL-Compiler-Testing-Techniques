
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(20, 16)
        self.key   = torch.nn.Linear(20, 16)
        self.value = torch.nn.Linear(16, 4)
 
    def forward(self, query, key):
        q_k = self.query(query).unsqueeze(-1).bmm(self.key(key))  # Compute the dot product of the query and key tensors
        qk   = torch.nn.functional.softmax(q_k, dim=-1)          # Apply softmax to the scaled dot product
        output = qk.matmul(self.value(key)).squeeze(-1)  # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()
x1 = torch.randn(1, 20)
y1 = torch.randn(4)
