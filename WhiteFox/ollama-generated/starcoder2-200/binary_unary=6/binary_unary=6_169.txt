
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 256)
 
    def forward(self, x1):
        v1  = self.linear1(x1)
        v2  = v1 - other  # 'other' is a value used for validation. It could be any number.
        return  torch.nn.functional.relu(v2)

# Initializing the model
m = Model()


# Inputs to the model