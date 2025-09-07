
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Embedding(4, 20)
        self.key    = torch.nn.Embedding(6, 30)
        self.value  = torch.nn.Embedding(15, 20)
 
    def forward(self, x1, x2):
        query = self.query(x1)
        key   = self.key(x2)
        value = self.value(x1 + x2)
        return torch.matmul(query, key), (value * 0.5).softmax()


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randint(2, 4)
x2 = torch.randint(3, 6)
