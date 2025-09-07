
class Model(torch.nn.Module):
    def __init__(self, n):
        super().__init__()
        self.split  = [n] * 8
        self.cat  = torch.nn.Linear(in_features=16, out_features=32)
 
    def forward(self, x1):
        split_tensors  = torch.split(x1, self.split, dim=-1)
        concatenated_tensor  = torch.cat([split_tensors[i] for i in range(len(self.split))], dim=-1)
        v2  = self.cat(concatenated_tensor)
        return v2


# Initializing the model
m  = Model(3)

# Inputs to the model
x1  = torch.randn(1, 48)
__output__  = m(x1)

