
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(512, 8) # A linear transformation layer that maps from the output of the previous model to a single vector for each query
        self.key = torch.nn.Linear(512, 8) 
        self.value = torch.nn.Linear(512, 8)
 
    def forward(self, x):
        # Query: Compute the weighted sum of all the heads. The weights will be computed as the softmax of the scaled dot product of the query and key tensors. 
        qk = self.query(x).matmul(self.key(x).transpose(-2, -1)) / math.sqrt(512) # (batch_size x 8) @ (512 x 8), then scale it
        attn_weight = torch.softmax(qk, dim=-1) # Softmax to the result of the scaled dot product and (batch_size x 64 x 64)
        output = torch.matmul(attn_weight, self.value(x)) # Compute the dot product of the attention weights and the value
        return output

# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 512, 64, 64)
