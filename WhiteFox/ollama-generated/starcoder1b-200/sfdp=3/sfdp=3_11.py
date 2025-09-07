
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(1024, 256)
        self.key = torch.nn.Linear(1024, 128)
 
    def forward(self, x1):
        v1 = self.query(x1)
        v2 = self.key(x1) * 0.5
        v3 = torch.tanh(v2)
        v4 = torch.nn.functional.dropout(v3, p=dropout_p)
        v5 = torch.matmul(v4, value)
        return v5


# Initializing the model
m = Model()

