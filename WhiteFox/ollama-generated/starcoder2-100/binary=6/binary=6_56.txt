
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 5)
 
    def forward(self, x1):
        v1 = self.linear1(x1)
        v2 = v1 - 0
        return v2


# Initializing the model and printing the input_tensor to the model
m  = Model()
print(m)

