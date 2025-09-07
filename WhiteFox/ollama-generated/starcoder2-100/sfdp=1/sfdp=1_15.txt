
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dot1 = torch.nn.Linear(7, 3)

    def forward(self, query, key, value):
        v2  = torch.nn.functional.normalize(query)
        v3  = self.dot1(v2)
        return v3

# Initializing the model
m = Model()

 # Inputs to the model
query = torch.randn(8,7 )
key   = query.clone().detach() + 0.5
value = key

