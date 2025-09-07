
class Model(torch.nn.Module):
    def __init__(self, num_features):
        super().__init__()
        self.fc1 = torch.nn.Linear(num_features, 256)
        self.fc2 = torch.nn.Linear(256, 10)
 
    def forward(self, x1):
        t1  = x1.flatten()
        t2  = t1.view(t1.shape[0], -1)
        t3  = self.fc1(t2)
        t4  = torch.nn.functional.softmax(t3, dim=-1)
        t5  = self.fc2(torch.mm(t3.view(t3.shape[0], -1), t4))
        return t5


# Initializing the model
m = Model(num_features=64*64)

# Inputs to the model
x1  = torch.randn(1, 64, 64)
