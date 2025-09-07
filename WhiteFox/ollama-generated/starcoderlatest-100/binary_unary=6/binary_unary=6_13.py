
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64*64, 80)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(-1))
        v2 = v1 - other_tensor
        v3 = torch.relu(v2)
        return v3


# Inputs to the model
x1 = torch.randn(batch_size, 64*64)
