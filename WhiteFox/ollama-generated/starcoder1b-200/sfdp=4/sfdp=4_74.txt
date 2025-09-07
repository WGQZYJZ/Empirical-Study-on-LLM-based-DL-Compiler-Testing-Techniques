
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(768, 10)
        self.key = torch.nn.Linear(32, 4)
        self.value = torch.nn.Linear(4, 5)
 
    def forward(self, x1, x2):
        query = self.query(x1)
        key = self.key(x2)
        value = self.value(x1)
        return (query @ key).softmax(-1) * value


# Initializing the model
m  = Model()
