
class Model(torch.nn.Module):
    def __init__(self, d_model=128):
        super().__init__()
        self.linear_q = torch.nn.Linear(d_model, d_model)
        self.linear_k = torch.nn.Linear(d_model, d_model)
        self.linear_v = torch.nn.Linear(d_model, d_model)
        self.dropout = torch.nn.Dropout(p=0.15)
 
    def forward(self, x, y):
        q  = self.linear_q(x)
        k  = self.linear_k(y)
        v  = self.linear_v(y)
        d_k = torch.div(torch.norm(k, p=2), math.sqrt(d_model)) # Calculate the norm of k over time, i.e., sqrt(d_model)
        dk = torch.diag(1/d_k) # Create diagonal matrix for each timestep. (dk: d_k for every time step d)
        dk = self.dropout(dk)  # Apply dropout to the diagonal matrix
        
        return dk.matmul(v)


# Initializing the model
m = Model()


# Inputs to the model
q = torch.randn(1, 8, 64, 64)
k = torch.randn(2, 8, 64, 64) # Input dimension: 2 x d_model
