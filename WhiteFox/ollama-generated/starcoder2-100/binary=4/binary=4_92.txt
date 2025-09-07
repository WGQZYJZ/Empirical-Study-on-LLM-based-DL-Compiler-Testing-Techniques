
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 10, 4)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + self.__other__ # This is the other tensor mentioned above
        return v2


# Initializing the model