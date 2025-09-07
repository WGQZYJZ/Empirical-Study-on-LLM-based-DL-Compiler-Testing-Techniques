
class Model(torch.nn.Module):
    def __init__(self, dim=1024, num_heads=8):
        super().__init__()
        self.dim = dim
        self.num_heads = num_heads
        self.fc1 = torch.nn.Linear(dim, dim)
        self.fc2 = torch.nn.Linear(dim, dim * 4)
        self.fc3 = torch.nn.Linear(dim * 4, dim * 8)
        self.fc4 = torch.nn.Linear(dim * 8, dim * 8)
        self.fc5 = torch.nn.Linear(dim * 8, dim)
        self.dropout = torch.nn.Dropout(0.3)
 
    def forward(self, x1):
        qk  = torch.matmul(x1, x1.transpose(-2, -1)) / math.sqrt(self.dim)
        v  = torch.matmul(x1, x1)
        k = kq  * self.num_heads
        scaled_qk  = k.div(math.sqrt(float(self.dim))) 
        k  = scaled_qk.softmax(-2)
        v  = torch.matmul(k, v)
        v  = self.dropout(v).contiguous().view(-1, self.num_heads, self.dim)
        k  = scaled_qk.softmax(-1)
        output = torch.matmul(v, k).contiguous().view(-1, self.num_heads, self.dim * 8)
        return output


# Initializing the model
m = Model()


