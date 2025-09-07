
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 4)

    def forward(self, x1): # x1: [b, in_features]
        v1 = x1.permute(0, 2, 1).clone() # [b, 3, 2]
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias) 
        return v2

m = Model()
