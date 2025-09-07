
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul = torch.nn.Linear(768, 3072)
 
    def forward(self, x1):
        v1 = torch.matmul(x1, self.matmul.weight).add(self.matmul.bias).unsqueeze(-1) # Shape: (batch_size, seq_len, 1)
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(240, 768)
