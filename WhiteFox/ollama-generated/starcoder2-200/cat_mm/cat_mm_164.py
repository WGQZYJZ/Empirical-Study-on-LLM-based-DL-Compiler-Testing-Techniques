torch.Size([2, 784]) torch.Size([784])
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(784, 50)
 
    def forward(self, x1):
        v1  = x1[0] * x1[1].view(-1) 
        return [v1 for i in range(3)]

 # Initializing the model
m  = Model()
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)
 
    def forward(self, x1):
         # Matrix multiplication of two input tensors
        v1 = torch.mm(x1[0], x1[1])
        return [v1 for i in range(3)]

 # Initializing the model
m  = Model()
