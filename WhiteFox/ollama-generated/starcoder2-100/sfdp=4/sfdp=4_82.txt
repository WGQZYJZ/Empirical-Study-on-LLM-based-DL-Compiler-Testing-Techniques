
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(20, 5)
        self.key = torch.nn.Linear(21, 4)

    def forward(self, query):
        v1  = torch.softmax(torch.stack([self.query(query),
                                         self.key(query)], dim=0),
                            dim=-1)

        return (v1 @ query) / math.sqrt(20 + 5)

# Initializing the model
m = Model()


# Inputs to the model
query_tensor  = torch.randn(3, 20)
query__output = m(query_tensor)

# Input 1 to the function
__inputs__  = [torch.randn(3, 4)]


