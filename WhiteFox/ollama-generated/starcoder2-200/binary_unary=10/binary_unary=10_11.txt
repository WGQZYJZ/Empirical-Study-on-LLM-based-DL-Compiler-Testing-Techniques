
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(327680, 1)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + other_tensor
        v3  = torch.relu(v2)
        return v3

# Initializing the model
m = Model()
other_tensor  = torch.randn([8, 3]) # arbitrary input tensor to add to the result of linear transformation

