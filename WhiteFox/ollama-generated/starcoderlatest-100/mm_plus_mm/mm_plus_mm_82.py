
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(4096, 512)
        self.fc2 = torch.nn.Linear(512, 256)
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x3, x4)
        v3 = v1 + v2 
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(512)  # input_tensor_1
x2 = torch.randn(2048) # input_tensor_2
x3 = torch.randn(2048) # input_tensor_3
x4 = torch.randn(2048) # input_tensor_4
