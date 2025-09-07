import torch 

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, p=0.5) # Apply dropout to the input tensor and then use this new tensor as an argument of the linear transformation function
        v2 = self.linear(v1)
        return v2
