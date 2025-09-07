
class Model(torch.nn.Module):
    def __init__(self, d_k=16, nhead=8):
        super().__init__()
        self.d_k = d_k
        self.nhead = nhead
        
        # Query Layer
        self.query = torch.nn.Linear(d_model, d_k)

        # Key Layer
        self.key = torch.nn.Linear(d_model, d_k)

        # Value Layer
        self.value = torch.nn.Linear(d_model, d_k)

        # Scale Factor Layer
        self.scale_factor = torch.nn.Parameter(torch.randn(1), requires_grad=True)
        
        # Softmax Layer (Normalization for numerical stability)
        self.softmax = torch.nn.Softmax(dim=-1)

    def forward(self, x1, x2):
        # Compute the dot product of the query and the key. 
        # Scaled by an inverse scale factor.
        scaled_qk = torch.matmul(x1, x2.transpose(-2, -1)) 
        
        # Apply softmax to compute probabilities of values in each column.
        dropout_qk = torch.nn.functional.dropout(scaled_qk, p=0.5)
        output = self.softmax(dropout_qk)

        return output * self.scale_factor

# Initializing the model
model = Model()
x1 = torch.randn(2, 3, 64, 64)
x2 = torch.randn(2, 3, 64, 64)
