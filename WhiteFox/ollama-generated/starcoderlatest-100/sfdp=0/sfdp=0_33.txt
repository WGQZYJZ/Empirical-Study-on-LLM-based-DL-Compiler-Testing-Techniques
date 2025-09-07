
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.key = torch.nn.Parameter(torch.randn(4096, 32))
        self.query = torch.nn.Parameter(torch.randn(16, 32))
 
    def forward(self, x1):
        v1 = torch.matmul(x1, self.key)
        v2 = v1 / math.sqrt(v1.size(-1)) # Scale the output to unit length
        v3 = torch.softmax(v2, dim=-1)
        v4 = torch.matmul(self.query, v3.transpose(-2, -1)) # Compute the scaled dot product between query and key
        output = torch.matmul(v4, self.value).unsqueeze(0)
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(16, 32, 16, 16)
