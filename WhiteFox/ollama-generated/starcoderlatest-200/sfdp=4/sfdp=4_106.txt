
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(3, 8) # This linear layer has a weight and bias matrix
        self.key = torch.nn.Linear(3, 16)
        self.value = torch.nn.Linear(2048, 64)
 
    def forward(self, x1, x2):
        qk = self.query(x1) @ self.key.transpose(-2, -1) / math.sqrt(self.query.in_features)
        v1 = torch.cat((qk, self.value(x2)), dim=2)
        v2 = self.attention(v1)
        return v2
 
    def attention(self, x):
        qk = self.query(x) @ self.key.transpose(-2, -1) / math.sqrt(self.query.in_features)
        v1 = torch.cat((qk, self.value(x)), dim=2)
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        output = attn_weight @ v1
        return output
 

# Initializing the model
m = Model()
 
