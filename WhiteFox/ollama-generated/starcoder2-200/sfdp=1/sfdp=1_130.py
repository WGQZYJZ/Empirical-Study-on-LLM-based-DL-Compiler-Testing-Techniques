
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk = torch.nn.Linear(128, 3072)
 
    def forward(self, x):
        v1 = torch.matmul(x, self.qk.weight) # Computing the dot product of the query and key tensors
        v2 = v1 / math.sqrt(256.) 
        v3 = v2 + torch.nn.functional.dropout(v2, p=0.1) # Apply dropout to the softmax output
        return torch.matmul(v3, x[:, :, None].permute(-1, 1).repeat(1, 1, self.qk.weight.shape[-1]).permute([0, 2])) 


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(364987)
