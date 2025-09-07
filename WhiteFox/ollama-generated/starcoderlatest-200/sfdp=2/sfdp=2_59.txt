
class Model(torch.nn.Module):
    def __init__(self, query_dim=64):
        super().__init__()
        self.query = torch.nn.Linear(query_dim, 8)
        self.key   = torch.nn.Linear(query_dim, 8)
        self.value = torch.nn.Linear(query_dim, 8)
 
    def forward(self, query):
        v1 = torch.matmul(query, self.query.weight.unsqueeze(-2))
        v2 = torch.matmul(query, self.key.weight.unsqueeze(-2))
        v3 = torch.matmul(query, self.value.weight.unsqueeze(-2))
        output = torch.cat((v1, v2, v3), dim=-1)
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 64, 3072) # Shape (N, C, H, W)
