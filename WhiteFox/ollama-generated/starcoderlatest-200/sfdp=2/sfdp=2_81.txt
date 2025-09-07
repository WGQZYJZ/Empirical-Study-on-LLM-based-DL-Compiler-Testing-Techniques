
class Attention(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.dim = dim
 
    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk / (math.sqrt(float(key.shape[-1]))) # Scale the dot product by the inverse scale factor
        softmax_qk = F.softmax(scaled_qk, dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5)
        output = torch.matmul(dropout_qk, value)
        return output
 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(8, 24)
        self.attention = Attention(24)
        self.dropout = torch.nn.Dropout(p=0.5)
 
    def forward(self, x):
        v = self.attention(x, x, x) # This will apply the dot product attention function
        return self.dropout(F.relu(self.linear1(v)))
 
m = Model()


