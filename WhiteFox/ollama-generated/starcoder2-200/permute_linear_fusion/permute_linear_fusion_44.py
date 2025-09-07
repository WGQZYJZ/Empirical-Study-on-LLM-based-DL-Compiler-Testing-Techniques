
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 1)

    def forward(self, x1):
        v0  = x1.clone()
        v1  = x1.permute(0, 3, 1) # Permute the input tensor
        v4  = self.linear(v1).relu() 
        v5  = torch.nn.functional.softmax(x2, dim=2) 
        return v6


# Initializing the model