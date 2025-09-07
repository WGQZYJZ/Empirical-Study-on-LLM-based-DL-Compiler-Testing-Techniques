
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 8)
        self.linear2 = torch.nn.Linear(760, 5349)
 
    def forward(self, input_tensor1):
        t1 = torch.mm(input_tensor1, 0.0001) 
        v1 = self.linear1(t1) + t1 
        v2 = self.linear2(v1) 
        return v2

# Initializing the model and obtaining input tensor from user
m  = Model()
x1  = torch.randn(3570, 4980).float()
