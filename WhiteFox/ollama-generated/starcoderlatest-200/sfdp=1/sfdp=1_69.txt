
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul = torch.nn.Linear(32, 64)
        self.dropout = torch.nn.Dropout(p=0.5)

    def forward(self, q1, k1, v1):
        output = self.matmul(q1 * k1).div(16).softmax(dim=-1)
        output = self.dropout(output)
        return output.matmul(v1)

# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(1, 32, 512, 512)
key   = torch.randn(1, 32, 512, 512)
value = torch.randn(1, 32, 512, 512)
