
class Model(torch.nn.Module):
    def __init__(self, n_heads, d_model, scale_factor, dropout=0.1):
        super().__init__()
        self.q = torch.nn.Linear(d_model, d_model, bias=False)
        self.k = torch.nn.Linear(d_model, d_model, bias=False)
        self.v = torch.nn.Linear(d_model, d_model, bias=False)
        self.o = torch.nn.Linear(d_model, d_model, bias=True)
        # For softmax
        self.scale_factor = scale_factor
 
    def forward(self, x):
        v1  = F.relu(self.q(x))
        v2  = F.relu(self.k(x))
        v3  = F.relu(self.v(x))
        # For softmax
        scaled_v1 = v1.div(self.scale_factor)
        scaled_v2 = v2.div(self.scale_factor)
        softmax_qk = scaled_v1.matmul(scaled_v2.transpose(-2, -1)).softmax(dim=-1)
        output  = torch.nn.functional.dropout(softmax_qk, p=dropout).matmul(v3) # Apply dropout to the softmax output
        return self.o(output)


# Initializing the model
m = Model(n_heads=8, d_model=128, scale_factor=4096)

# Inputs to the model
x = torch.randn(1, 3, 512, 512)
