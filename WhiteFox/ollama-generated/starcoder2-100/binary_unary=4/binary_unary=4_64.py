
class Model(torch.nn.Module):
    def __init__(self, **kwargs):
        super().__init__()
        self.linear = torch.nn.Linear(32*32*4, 10)
        self.__other__  = kwargs['other']
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + self.__other__ 
        v3 = torch.relu(v2)
        return v3

# Initializing the model<|end_of_code|>
m  = Model(**{'other':torch.randn(4, 10)})

