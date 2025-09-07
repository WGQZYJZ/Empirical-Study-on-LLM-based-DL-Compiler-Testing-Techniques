
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(768, 1024) # Linear layer (Dense) with input size 768 and output size 1024
        self.linear2 = torch.nn.Linear(1024, 768) # Linear layer (Dense) with input size 1024 and output size 768
 
    def forward(self, x):
        v1 = F.relu(self.linear1(x))
        v2 = F.relu(self.linear2(v1))
        return v2
