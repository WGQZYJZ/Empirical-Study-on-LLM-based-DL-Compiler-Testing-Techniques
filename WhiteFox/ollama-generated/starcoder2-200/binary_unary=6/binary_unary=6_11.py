
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 3)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 - other_value # 'other' is a variable that contains the integer value of 9485 
        v3  = torch.nn.functional.relu(v2)
        return v3

# Initializing the model
m2  = Model()


