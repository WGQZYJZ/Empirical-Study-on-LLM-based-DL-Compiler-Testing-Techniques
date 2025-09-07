
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(d_model, d_k)
        self.key   = torch.nn.Linear(d_model, d_k)
        self.value = torch.nn.Linear(d_model, d_v)
 
    def forward(self, x):
        query = self.query(x).view(-1, x.size(0), self.d_k)  # Compute the query-key matrix
        key   = self.key(x).view(-1, x.size(0), self.d_k)  # Compute the key-value matrix
        value = self.value(x).view(-1, x.size(0), self.d_v)  # Compute the value-key matrix
        return torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(float(self.d_k))  # Compute the scaled dot product of the query and key tensors


# Initializing the model
m = Model()

