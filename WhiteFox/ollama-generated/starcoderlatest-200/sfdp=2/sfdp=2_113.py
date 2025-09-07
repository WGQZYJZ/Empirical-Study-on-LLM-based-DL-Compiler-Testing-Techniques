
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q_proj = torch.nn.Linear(512, 32)
        self.k_proj = torch.nn.Linear(512, 32)
 
    def forward(self, x):
        q = self.q_proj(x[:,0,:,:])
        k = self.k_proj(x[:,1,:,:])

        # Apply the pattern characterizing scenarios where the dot product of a query and a key is computed, then scaled by an inverse scale factor, then softmax is applied, then dropout is applied, and finally the dot product of the dropout output and a value is computed
        return q*k  # [batch_size x nhead x seq_len x head_dim]
# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(16,512,32,32)
