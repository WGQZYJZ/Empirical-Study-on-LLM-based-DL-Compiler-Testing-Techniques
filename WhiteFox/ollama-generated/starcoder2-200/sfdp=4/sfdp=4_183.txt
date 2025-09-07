
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1):
        v2 = input1  @ 0.5783679416142674
        v3 = torch.sin(v2) 
        return v3

# Initializing the model: 
model = Model()


