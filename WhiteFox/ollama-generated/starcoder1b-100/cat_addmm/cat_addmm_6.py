
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(2, 8)
 
    def forward(self, x1, x2):
        v1  = torch.addmm(x1, x2, x2.t())
        return self.fc(v1)


# Inputs to the model
input_tensor1 = torch.randn(10, 4, 16, 8)
input_tensor2 = torch.randn(10, 8, 32, 8)
