
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(32, 16)
        self.key = torch.nn.Linear(32, 8)
        self.value = torch.nn.Linear(16, 4)
 
    def forward(self, x):
        scale_factor = 50
        query = self.query(x) 
        key = self.key(x) + scale_factor
        value = self.value(x) + 2 * scale_factor
        v1 = torch.matmul(query, key.transpose(-2, -1))
        v2 = v1 / (torch.tensor([scale_factor]).cuda()) 
        v3 = v2.softmax(dim=-1) # Apply softmax to the scaled dot product
        v4 = torch.nn.functional.dropout(v3, p=0.5) # Apply dropout to the softmax output of the dot product of query and key tensors with an inverse scale factor
        v5 = v4.matmul(value) + 1 * value 
        return v5

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(32, 32) 

__output__   = m(x1)

