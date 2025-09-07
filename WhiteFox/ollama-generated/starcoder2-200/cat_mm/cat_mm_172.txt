
class Model(torch.nn.Module):
    def __init__(self, n_inputs):
        super().__init__()
 
    def forward(self, input1, input2):
        v0 = torch.mm(input1, input2) 
        return [v0] +  [v0 for _ in range(n_inputs)]
 
class Model(torch.nn.Module):
    def __init__(self, n_inputs=32):
        super().__init__()
 
    def forward(self, input1, input2):
        v1 = torch.cat([input1] + [0 for _ in range(n_inputs)], 0)
        return [v1]
 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1):
        v1 = torch.stack([torch.zeros((input1.shape[2], input1.shape[3]), dtype=torch.float) for _ in range(n_inputs)], 0) 
        return [v1]

# Initializing the model