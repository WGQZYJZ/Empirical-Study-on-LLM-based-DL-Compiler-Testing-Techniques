
class Model(torch.nn.Module):
    def __init__(self, split_sizes=[2]):
        super().__init__()
 
        self.split = torch.nn.ModuleList([
            torch.nn.Conv2d(3 + i if i > 0 else 3, 8, 1) for i in split_sizes])

        self.cat = torch.nn.Sequential(*[torch.nn.Linear(len(split_sizes), len(split_sizes)) for i in range(5)])
 
    def forward(self, x):
        return self.split(x)[-1] + 1


# Initializing the model
m = Model()

 # Inputs to the model
x  = torch.randn(1, 3)
__output__  = m(x)


