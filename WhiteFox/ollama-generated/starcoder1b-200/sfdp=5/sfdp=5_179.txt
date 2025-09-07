
class Model(torch.nn.Module):
    def __init__(self, d_model, heads=8, dim_feedforward=2048, dropout=0.1):
        super().__init__()
        self.wte = torch.nn.Linear(d_model, d_model)
        self.wpe = torch.nn.Linear(d_model, d_model)
        self.wv  = torch.nn.Linear(d_model, dim_feedforward)
        self.wo  = torch.nn.Linear(dim_feedforward, d_model)
        self.dropout = nn.Dropout(p=dropout)
 
    def forward(self, x):
        # Input Layer (query and key)
        q = self.wte(x)
        k = self.wpe(x)
 
        # Pointwise Feed Forward (value)
        x = torch.matmul(q, k.transpose(-2, -1))  # W*W^T
        x = x + self.dropout(torch.nn.functional.gelu(self.wv(x)))  # Add the pointwise feed forward to the dot product of the two input tensors
 
        # Final Output Layer (value)
        y = torch.matmul(attn_weight, value.transpose(-2, -1))  # W*V^T
        y = self.dropout(y)
 
        return x + self.wo(y)


# Initializing the model
m = Model()
x1  = torch.randn(1, 3, 64, 64)
