
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1): # 1
        v3 = torch.permute(x1, 0, -2)  # 1
        v4 = torch.nn.functional.linear(v3, self.linear_1.weight, self.linear_1.bias) 
        return v4

# Initializing the model
m  = Model()

