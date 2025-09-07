
class Model(torch.nn.Module):
    def __init__(self, hidden_size=256):
        super().__init__()
        self.query = torch.nn.Linear(input_dim=64*3*11*11, output_dim=hidden_size)
        self.key   = torch.nn.Linear(input_dim=64*3*11*11, output_dim=hidden_size)
        self.value = torch.nn.Linear(input_dim=64*2*11*11, output_dim=hidden_size)
 
    def forward(self, x1):
        # Query Layer
        qk  = torch.matmul(x1, self.key.weight) / math.sqrt(float(self.key.out_features))
        softplus_qk  = F.softplus(qk)  # Apply softmax to the scaled dot product
        dropout_qk   = nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        # Value Layer
        v1 = torch.matmul(x1, self.value.weight) / math.sqrt(float(self.value.out_features))
 
        return v1
 

# Initializing the model
m = Model()

